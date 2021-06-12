# Copyright 2020 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This script performs lighthouse checks and creates lighthouse reports.
Any callers must pass in a flag, either --accessibility or --performance.
"""

from __future__ import absolute_import  # pylint: disable=import-only-modules
from __future__ import unicode_literals  # pylint: disable=import-only-modules

import argparse
import os
import subprocess
import sys

from constants import constants
import python_utils
from scripts import build
from scripts import common
from scripts import servers


LIGHTHOUSE_MODE_PERFORMANCE = 'performance'
LIGHTHOUSE_MODE_ACCESSIBILITY = 'accessibility'
SERVER_MODE_PROD = 'dev'
SERVER_MODE_DEV = 'prod'
GOOGLE_APP_ENGINE_PORT = 8181
LIGHTHOUSE_CONFIG_FILENAMES = {
    LIGHTHOUSE_MODE_PERFORMANCE: '.lighthouserc.js',
    LIGHTHOUSE_MODE_ACCESSIBILITY: '.lighthouserc-accessibility.js'
}
APP_YAML_FILENAMES = {
    SERVER_MODE_PROD: 'app.yaml',
    SERVER_MODE_DEV: 'app_dev.yaml'
}

_PARSER = argparse.ArgumentParser(
    description="""
Run the script from the oppia root folder:
    python -m scripts.run_lighthouse_tests
Note that the root folder MUST be named 'oppia'.
""")

_PARSER.add_argument(
    '--mode', help='Sets the mode for the lighthouse tests',
    required=True, choices=['accessibility', 'performance'],)


def run_lighthouse_puppeteer_script():
    """Runs puppeteer script to collect dynamic urls."""
    puppeteer_path = (
        os.path.join('core', 'tests', 'puppeteer', 'lighthouse_setup.js'))
    bash_command = [common.NODE_BIN_PATH, puppeteer_path]

    try:
        script_output = subprocess.check_output(bash_command).split('\n')
    except subprocess.CalledProcessError:
        python_utils.PRINT(
            'Puppeteer script failed. More details can be found above.')
        sys.exit(1)
    else:
        python_utils.PRINT(script_output)
        for url in script_output:
            export_url(url)
        python_utils.PRINT('Puppeteer script completed successfully.')


def run_webpack_compilation():
    """Runs webpack compilation."""
    max_tries = 5
    webpack_bundles_dir_name = 'webpack_bundles'
    for _ in python_utils.RANGE(max_tries):
        try:
            with servers.managed_webpack_compiler() as proc:
                proc.wait()
        except subprocess.CalledProcessError as error:
            python_utils.PRINT(error.output)
            sys.exit(error.returncode)
            return
        if os.path.isdir(webpack_bundles_dir_name):
            break
    if not os.path.isdir(webpack_bundles_dir_name):
        python_utils.PRINT('Failed to complete webpack compilation, exiting...')
        sys.exit(1)


def export_url(url):
    """Exports the entity ID in the URL to an environmental variable.

    Args:
        url: str. The URL to parse and extract the entity ID from. If no ID is
            present, nothing is exported to the environment.
    """
    url_parts = url.split('/')
    python_utils.PRINT('Parsing and exporting entity ID in URL: %s' % url)
    if 'collection_editor' in url:
        os.environ['collection_id'] = url_parts[5]
    elif 'create' in url:
        os.environ['exploration_id'] = url_parts[4]
    elif 'topic_editor' in url:
        os.environ['topic_id'] = url_parts[4]
    elif 'story_editor' in url:
        os.environ['story_id'] = url_parts[4]
    elif 'skill_editor' in url:
        os.environ['skill_id'] = url_parts[4]
    else:
        return


def run_lighthouse_checks(lighthouse_mode):
    """Runs the lighthouse checks through the .lighthouserc.js config.

    Args:
        lighthouse_mode: str. Represents whether the lighthouse checks are in
            accessibility mode or performance mode.
    """
    lhci_path = os.path.join('node_modules', '@lhci', 'cli', 'src', 'cli.js')
    bash_command = [
        common.NODE_BIN_PATH, lhci_path, 'autorun',
        '--config=%s' % LIGHTHOUSE_CONFIG_FILENAMES[lighthouse_mode],
    ]

    try:
        subprocess.check_call(bash_command)
        python_utils.PRINT('Lighthouse checks completed successfully.')
    except subprocess.CalledProcessError:
        python_utils.PRINT(
            'Lighthouse checks failed. More details can be found above.')
        sys.exit(1)


def main(args=None):
    """Runs lighthouse checks and deletes reports."""
    parsed_args = _PARSER.parse_args(args=args)

    if parsed_args.mode == LIGHTHOUSE_MODE_ACCESSIBILITY:
        lighthouse_mode = LIGHTHOUSE_MODE_ACCESSIBILITY
        server_mode = SERVER_MODE_DEV
    elif parsed_args.mode == LIGHTHOUSE_MODE_PERFORMANCE:
        lighthouse_mode = LIGHTHOUSE_MODE_PERFORMANCE
        server_mode = SERVER_MODE_PROD
    else:
        raise Exception(
            'Invalid parameter passed in: \'%s\', please choose'
            'from \'accessibility\' or \'performance\'' % parsed_args.mode)

    if lighthouse_mode == LIGHTHOUSE_MODE_PERFORMANCE:
        python_utils.PRINT('Building files in production mode.')
        # We are using --source_maps here, so that we have at least one CI check
        # that builds using source maps in prod env. This is to ensure that
        # there are no issues while deploying oppia.
        build.main(args=['--prod_env', '--source_maps'])
    elif lighthouse_mode == LIGHTHOUSE_MODE_ACCESSIBILITY:
        build.main(args=[])
        run_webpack_compilation()

    with python_utils.ExitStack() as stack:
        stack.enter_context(common.inplace_replace_file_context(
            common.CONSTANTS_FILE_PATH,
            '"ENABLE_ACCOUNT_DELETION": .*',
            '"ENABLE_ACCOUNT_DELETION": true,'))

        stack.enter_context(servers.managed_redis_server())
        stack.enter_context(servers.managed_elasticsearch_dev_server())

        if constants.EMULATOR_MODE:
            stack.enter_context(servers.managed_firebase_auth_emulator())

        stack.enter_context(servers.managed_dev_appserver(
            APP_YAML_FILENAMES[server_mode],
            port=GOOGLE_APP_ENGINE_PORT,
            clear_datastore=True,
            log_level='critical',
            skip_sdk_update_check=True))

        run_lighthouse_puppeteer_script()
        run_lighthouse_checks(lighthouse_mode)


if __name__ == '__main__':
    main()
