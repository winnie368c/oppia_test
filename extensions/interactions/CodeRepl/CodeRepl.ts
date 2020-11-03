// Copyright 2019 The Oppia Authors. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS-IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/**
 * @fileoverview Requires for CodeRepl interaction.
 */

require('interactions/CodeRepl/static/code_repl.css');

require('interactions/CodeRepl/code-repl-prediction.service.ts');

require('interactions/CodeRepl/directives/code-repl-rules.service.ts');
require('interactions/CodeRepl/directives/code-repl-validation.service.ts');
require(
  'interactions/CodeRepl/directives/oppia-interactive-code-repl.directive.ts');
require(
  'interactions/CodeRepl/directives/' +
  'oppia-response-code-repl.directive.ts');
require(
  'interactions/CodeRepl/directives/' +
  'oppia-short-response-code-repl.directive.ts');