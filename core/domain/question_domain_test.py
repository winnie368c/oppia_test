# Copyright 2018 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, softwar
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for question domain objects."""

from __future__ import annotations

import copy
import datetime
import re

from core import feconf
from core import utils
from core.domain import customization_args_util
from core.domain import question_domain
from core.domain import state_domain
from core.domain import translation_domain
from core.tests import test_utils


class QuestionChangeTest(test_utils.GenericTestBase):
    """Test for Question Change object."""

    def test_to_dict(self):
        """Test to verify to_dict method of the Question Change object."""
        expected_object_dict = {
            'cmd': 'update_question_property',
            'property_name': 'question_state_data',
            'new_value': 'new_value',
            'old_value': 'old_value',
        }

        change_dict = {
            'cmd': 'update_question_property',
            'property_name': 'question_state_data',
            'new_value': 'new_value',
            'old_value': 'old_value',
        }
        observed_object = question_domain.QuestionChange(
            change_dict=change_dict,
        )

        self.assertEqual(expected_object_dict, observed_object.to_dict())

    def test_change_dict_without_cmd(self):
        """Test to verify __init__ method of the Question Change object
        when change_dict is without cmd key.
        """
        self.assertRaisesRegex(
            utils.ValidationError,
            'Missing cmd key in change dict',
            callableObj=question_domain.QuestionChange,
            change_dict={}
        )

    def test_change_dict_with_wrong_cmd(self):
        """Test to verify __init__ method of the Question Change object
        when change_dict is with wrong cmd value.
        """
        self.assertRaisesRegex(
            utils.ValidationError,
            'Command wrong is not allowed',
            callableObj=question_domain.QuestionChange,
            change_dict={'cmd': 'wrong', }
        )

    def test_change_dict_with_missing_attributes_in_cmd(self):
        """Test to verify __init__ method of the Question Change object
        when change_dict is with missing attributes in cmd.
        """
        self.assertRaisesRegex(
            utils.ValidationError,
            'The following required attributes are present: new_value',
            callableObj=question_domain.QuestionChange,
            change_dict={
                'cmd': 'update_question_property',
                'property_name': 'question_state_data',
                'old_value': 'old_value'
            }
        )

    def test_change_dict_with_extra_attributes_in_cmd(self):
        """Test to verify __init__ method of the Question Change object
        when change_dict is with extra attributes in cmd.
        """
        self.assertRaisesRegex(
            utils.ValidationError,
            'The following extra attributes are present: invalid',
            callableObj=question_domain.QuestionChange,
            change_dict={'cmd': 'create_new', 'invalid': 'invalid'}
        )

    def test_update_question_property_with_wrong_property_name(self):
        """Test to verify __init__ method of the Question Change object
        when cmd is update_question_property and wrong property_name is given.
        """
        self.assertRaisesRegex(
            utils.ValidationError, (
                'Value for property_name in cmd update_question_property: '
                'wrong is not allowed'),
            callableObj=question_domain.QuestionChange,
            change_dict={
                'cmd': 'update_question_property',
                'property_name': 'wrong',
                'new_value': 'new_value',
                'old_value': 'old_value'
            }
        )

    def test_create_new(self):
        """Test to verify __init__ method of the Question Change object
        when cmd is create_new.
        """
        change_dict = {
            'cmd': 'create_new'
        }
        observed_object = question_domain.QuestionChange(
            change_dict=change_dict,
        )

        self.assertEqual('create_new', observed_object.cmd)

    def test_update_question_property(self):
        """Test to verify __init__ method of the Question Change object
        when cmd is update_question_property.
        """
        change_dict = {
            'cmd': 'update_question_property',
            'property_name': 'question_state_data',
            'new_value': 'new_value',
            'old_value': 'old_value'
        }
        observed_object = question_domain.QuestionChange(
            change_dict=change_dict
        )

        self.assertEqual('update_question_property', observed_object.cmd)
        self.assertEqual('question_state_data', observed_object.property_name)
        self.assertEqual('new_value', observed_object.new_value)
        self.assertEqual('old_value', observed_object.old_value)

    def test_create_new_fully_specified_question(self):
        """Test to verify __init__ method of the Question Change object
        when cmd is create_new_fully_specified_question.
        """
        change_dict = {
            'cmd': 'create_new_fully_specified_question',
            'question_dict': {},
            'skill_id': '10',
        }
        observed_object = question_domain.QuestionChange(
            change_dict=change_dict,
        )

        self.assertEqual(
            'create_new_fully_specified_question', observed_object.cmd)
        self.assertEqual('10', observed_object.skill_id)
        self.assertEqual({}, observed_object.question_dict)

    def test_migrate_state_schema_to_latest_version(self):
        """Test to verify __init__ method of the Question Change object
        when cmd is migrate_state_schema_to_latest_version.
        """
        change_dict = {
            'cmd': 'migrate_state_schema_to_latest_version',
            'from_version': 0,
            'to_version': 10,
        }
        observed_object = question_domain.QuestionChange(
            change_dict=change_dict,
        )

        self.assertEqual(
            'migrate_state_schema_to_latest_version', observed_object.cmd)
        self.assertEqual(0, observed_object.from_version)
        self.assertEqual(10, observed_object.to_version)


class QuestionSuggestionChangeTest(test_utils.GenericTestBase):
    """Test for QuestionSuggestionChange object."""

    def test_to_dict(self):
        """Test to verify to_dict method of the Question Change object."""
        expected_object_dict = {
            'cmd': 'create_new_fully_specified_question',
            'question_dict': 'question_dict',
            'skill_id': 'skill_1',
            'skill_difficulty': '0.3'
        }

        change_dict = {
            'cmd': 'create_new_fully_specified_question',
            'question_dict': 'question_dict',
            'skill_id': 'skill_1',
            'skill_difficulty': '0.3'
        }
        observed_object = question_domain.QuestionSuggestionChange(
            change_dict=change_dict,
        )

        self.assertEqual(expected_object_dict, observed_object.to_dict())

    def test_change_dict_without_cmd(self):
        """Test to verify __init__ method of the QuestionSuggestionChange
        object when change_dict is without cmd key.
        """
        self.assertRaisesRegex(
            utils.ValidationError,
            'Missing cmd key in change dict',
            callableObj=question_domain.QuestionSuggestionChange,
            change_dict={}
        )

    def test_change_dict_with_wrong_cmd(self):
        """Test to verify __init__ method of the QuestionSuggestionChange object
        when change_dict is with wrong cmd value.
        """
        self.assertRaisesRegex(
            utils.ValidationError,
            'Command wrong is not allowed',
            callableObj=question_domain.QuestionSuggestionChange,
            change_dict={'cmd': 'wrong', }
        )

    def test_change_dict_with_missing_attributes_in_cmd(self):
        """Test to verify __init__ method of the QuestionSuggestionChange object
        when change_dict is with missing attributes in cmd.
        """
        self.assertRaisesRegex(
            utils.ValidationError,
            'The following required attributes are present: new_value',
            callableObj=question_domain.QuestionSuggestionChange,
            change_dict={
                'cmd': 'create_new_fully_specified_question',
                'question_dict': 'question_dict',
            }
        )

    def test_change_dict_with_extra_attributes_in_cmd(self):
        """Test to verify __init__ method of the QuestionSuggestionChange object
        when change_dict is with extra attributes in cmd.
        """
        self.assertRaisesRegex(
            utils.ValidationError,
            'The following extra attributes are present: invalid',
            callableObj=question_domain.QuestionSuggestionChange,
            change_dict={
                'cmd': 'create_new_fully_specified_question',
                'question_dict': 'question_dict',
                'skill_id': 'skill_1',
                'skill_difficulty': '0.3',
                'invalid': 'invalid'
            }
        )

    def test_create_new_fully_specified_question(self):
        """Test to verify __init__ method of the QuestionSuggestionChange object
        when cmd is create_new_fully_specified_question.
        """
        change_dict = {
            'cmd': 'create_new_fully_specified_question',
            'question_dict': {},
            'skill_id': '10',
            'skill_difficulty': '0.3',
        }
        observed_object = question_domain.QuestionSuggestionChange(
            change_dict=change_dict,
        )

        self.assertEqual(
            'create_new_fully_specified_question', observed_object.cmd)
        self.assertEqual('10', observed_object.skill_id)
        self.assertEqual({}, observed_object.question_dict)


class QuestionDomainTest(test_utils.GenericTestBase):
    """Tests for Question domain object."""

    def setUp(self):
        """Before each individual test, create a question."""
        super(QuestionDomainTest, self).setUp()
        question_state_data = self._create_valid_question_data('ABC')
        self.question = question_domain.Question(
            'question_id', question_state_data,
            feconf.CURRENT_STATE_SCHEMA_VERSION, 'en', 1, ['skill1'],
            ['skillId12345-123'])
        translation_dict = {
            'content_id_3': translation_domain.TranslatedContent(
                'My name is Nikhil.', True)
        }
        self.dummy_entity_translations = translation_domain.EntityTranslation(
            'exp_id', feconf.TranslatableEntityType.EXPLORATION, 1, 'en',
            translation_dict)

    def test_to_and_from_dict(self):
        """Test to verify to_dict and from_dict methods
        of Question domain object.
        """
        default_question_state_data = (
            question_domain.Question.create_default_question_state())
        question_dict = {
            'id': 'col1.random',
            'question_state_data': default_question_state_data.to_dict(),
            'question_state_data_schema_version': (
                feconf.CURRENT_STATE_SCHEMA_VERSION),
            'language_code': 'en',
            'version': 1,
            'linked_skill_ids': ['skill1'],
            'inapplicable_skill_misconception_ids': ['skill1-123']
        }

        observed_object = question_domain.Question.from_dict(question_dict)
        self.assertEqual(question_dict, observed_object.to_dict())

    def _assert_validation_error(self, expected_error_substring):
        """Checks that the skill passes strict validation."""
        with self.assertRaisesRegex(
            utils.ValidationError, expected_error_substring
        ):
            self.question.validate()

    def test_strict_validation(self):
        """Test to verify validate method of Question domain object with
        strict as True.
        """
        state = self.question.question_state_data
        state.interaction.solution = None
        self._assert_validation_error(
            'Expected the question to have a solution')
        state.interaction.hints = []
        self._assert_validation_error(
            'Expected the question to have at least one hint')
        state.interaction.default_outcome.dest = 'abc'
        self._assert_validation_error(
            'Expected all answer groups to have destination as None.')
        state.interaction.default_outcome.labelled_as_correct = False
        self._assert_validation_error(
            'Expected at least one answer group to have a correct answer')

    def test_strict_validation_for_answer_groups(self):
        """Test to verify validate method of Question domain object with
        strict as True for interaction with answer group.
        """
        state = self.question.question_state_data
        state.interaction.default_outcome.labelled_as_correct = False
        state.interaction.answer_groups = [
            state_domain.AnswerGroup.from_dict({
                'outcome': {
                    'dest': 'abc',
                    'feedback': {
                        'content_id': 'feedback_1',
                        'html': '<p>Feedback</p>'
                    },
                    'labelled_as_correct': True,
                    'param_changes': [],
                    'refresher_exploration_id': None,
                    'missing_prerequisite_skill_id': None
                },
                'rule_specs': [{
                    'inputs': {
                        'x': {
                            'contentId': 'rule_input_4',
                            'normalizedStrSet': ['Test']
                        }
                    },
                    'rule_type': 'Contains'
                }],
                'training_data': [],
                'tagged_skill_misconception_id': None
            })
        ]

        self._assert_validation_error(
            'Expected all answer groups to have destination as None.')

    def test_validate_invalid_list_of_inapplicable_skill_misconception_ids(
            self):
        """Test to verify that the validation fails when
        inapplicable_skill_misconception_ids value is an invalid list.
        """
        self.question.inapplicable_skill_misconception_ids = ['Test', 1]
        self._assert_validation_error(
            re.escape(
                'Expected inapplicable_skill_misconception_ids to be a list of '
                'strings, received [\'Test\', 1]'))

    def test_validate_invalid_type_of_inapplicable_skill_misconception_ids(
            self):
        """Test to verify that the validation fails when
        inapplicable_skill_misconception_ids value is an invalid type.
        """
        self.question.inapplicable_skill_misconception_ids = 123
        self._assert_validation_error(
            'Expected inapplicable_skill_misconception_ids to be a list of '
            'strings, received 123')

    def test_validate_invalid_format_of_inapplicable_skill_misconception_ids(
            self):
        """Test to verify that the validation fails when
        inapplicable_skill_misconception_ids value is an invalid format i.e.
        it is not of the form <skill-id>-<misconception-id>.
        """
        self.question.inapplicable_skill_misconception_ids = ['abc', 'def']
        self._assert_validation_error(
            re.escape(
                'Expected inapplicable_skill_misconception_ids to be a list '
                'of strings of the format <skill_id>-<misconception_id>, '
                'received [\'abc\', \'def\']'))

    def test_validate_duplicate_inapplicable_skill_misconception_ids_list(
            self):
        """Test to verify that the validation fails when
        inapplicable_skill_misconception_ids list is has duplicate values.
        """
        self.question.inapplicable_skill_misconception_ids = [
            'skillid12345-1', 'skillid12345-1']
        self._assert_validation_error(
            'inapplicable_skill_misconception_ids has duplicate values')

    def test_strict_validation_passes(self):
        """Test to verify validate method of a finalized Question domain object
        with correct input.
        """
        self.question.validate()

    def test_not_strict_validation(self):
        """Test to verify validate method of Question domain object with
        strict as False.
        """
        self.question.language_code = 'abc'
        self._assert_validation_error('Invalid language code')

        self.question.question_state_data = 'State data'
        self._assert_validation_error(
            'Expected question state data to be a State object')

        self.question.question_state_data_schema_version = 'abc'
        self._assert_validation_error(
            'Expected schema version to be an integer')

        self.question.question_state_data_schema_version = 45
        self._assert_validation_error(
            'Expected question state schema version to be %s, received '
                '%s' % (
                    feconf.CURRENT_STATE_SCHEMA_VERSION,
                    self.question.question_state_data_schema_version))

        self.question.linked_skill_ids = 'Test'
        self._assert_validation_error(
            'Expected linked_skill_ids to be a list of strings')

        self.question.linked_skill_ids = None
        self._assert_validation_error(
            'inked_skill_ids is either null or an empty list')

        self.question.linked_skill_ids = []
        self._assert_validation_error(
            'linked_skill_ids is either null or an empty list')

        self.question.linked_skill_ids = ['Test', 1]
        self._assert_validation_error(
            'Expected linked_skill_ids to be a list of strings')

        self.question.linked_skill_ids = ['skill1', 'skill1']
        self._assert_validation_error(
            'linked_skill_ids has duplicate skill ids')

        self.question.language_code = 1
        self._assert_validation_error('Expected language_code to be a string')

        self.question.version = 'abc'
        self._assert_validation_error('Expected version to be an integer')

        self.question.id = 123
        self._assert_validation_error('Expected ID to be a string')

    def test_create_default_question(self):
        """Test to verify create_default_question method of the Question domain
        object.
        """
        question_id = 'col1.random'
        skill_ids = ['test_skill1', 'test_skill2']
        question = question_domain.Question.create_default_question(
            question_id, skill_ids)
        default_question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        self.assertEqual(question.id, question_id)
        self.assertEqual(
            question.question_state_data.to_dict(), default_question_data)
        self.assertEqual(question.language_code, 'en')
        self.assertEqual(question.version, 0)
        self.assertEqual(question.linked_skill_ids, skill_ids)

    def test_update_language_code(self):
        """Test to verify update_language_code method of the Question domain
        object.
        """
        self.question.update_language_code('pl')

        self.assertEqual('pl', self.question.language_code)

    def test_update_linked_skill_ids(self):
        """Test to verify update_linked_skill_ids method of the Question domain
        object.
        """
        self.question.update_linked_skill_ids(['skill_id1'])

        self.assertEqual(['skill_id1'], self.question.linked_skill_ids)

    def test_update_inapplicable_skill_misconception_ids(self):
        """Test to verify update_inapplicable_skill_misconception_ids method
        of the Question domain object.
        """
        self.assertEqual(
            ['skillId12345-123'],
            self.question.inapplicable_skill_misconception_ids)
        self.question.update_inapplicable_skill_misconception_ids(
            ['skillid-misconceptionid'])
        self.assertEqual(
            ['skillid-misconceptionid'],
            self.question.inapplicable_skill_misconception_ids)

    def test_update_question_state_data(self):
        """Test to verify update_question_state_data method of the Question
        domain object.
        """
        question_state_data = self._create_valid_question_data('Test')

        self.question.update_question_state_data(question_state_data)

        self.assertEqual(
            question_state_data.to_dict(),
            self.question.question_state_data.to_dict()
        )

    def test_question_state_dict_conversion_from_v27_to_v28(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        test_data = question_data['recorded_voiceovers']
        question_data['content_ids_to_audio_translations'] = (
            test_data['voiceovers_mapping'])

        # Removing 'recorded_voiceovers' from question_data.
        del question_data['recorded_voiceovers']

        test_value = {
            'state': question_data,
            'state_schema_version': 27
        }

        self.assertNotIn('recorded_voiceovers', test_value['state'])

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 28)
        self.assertIn('recorded_voiceovers', test_value['state'])
        self.assertEqual(
            test_value['state']['recorded_voiceovers'], test_data)

    def test_question_state_dict_conversion_from_v28_to_v29(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        # Removing 'solicit_answer_details' from question_data.
        del question_data['solicit_answer_details']

        test_value = {
            'state': question_data,
            'state_schema_version': 28
        }

        self.assertNotIn('solicit_answer_details', test_value['state'])

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 29)
        self.assertIn('solicit_answer_details', test_value['state'])
        self.assertEqual(
            test_value['state']['solicit_answer_details'], False)

    def test_question_state_dict_conversion_from_v29_to_v30(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        question_data['interaction']['answer_groups'] = [
            {
                'tagged_misconception_id': 1
            }
        ]

        test_value = {
            'state': question_data,
            'state_schema_version': 29
        }

        self.assertIn(
            'tagged_misconception_id',
            test_value['state']['interaction']['answer_groups'][0]
        )

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 30)
        self.assertNotIn(
            'tagged_misconception_id',
            test_value['state']['interaction']['answer_groups'][0]
        )
        self.assertIn(
            'tagged_skill_misconception_id',
            test_value['state']['interaction']['answer_groups'][0]
        )
        self.assertIsNone(test_value['state']['interaction'][
            'answer_groups'][0]['tagged_skill_misconception_id'])

    def test_question_state_dict_conversion_from_v30_to_v31(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        question_data['recorded_voiceovers']['voiceovers_mapping'] = {
            'content': {
                'audio_metadata': {}
            }
        }

        test_value = {
            'state': question_data,
            'state_schema_version': 30
        }

        self.assertNotIn(
            'duration_secs',
            test_value['state']['recorded_voiceovers']['voiceovers_mapping'][
                'content']['audio_metadata']
        )

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 31)
        self.assertIn(
            'duration_secs',
            test_value['state']['recorded_voiceovers']['voiceovers_mapping'][
                'content']['audio_metadata']
        )
        self.assertEqual(
            test_value['state']['recorded_voiceovers']['voiceovers_mapping'][
                'content']['audio_metadata']['duration_secs'],
            0.0
        )

    def test_question_state_dict_conversion_from_v31_to_v32(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        question_data['interaction']['id'] = 'SetInput'

        test_value = {
            'state': question_data,
            'state_schema_version': 31
        }

        self.assertEqual(
            question_data['interaction']['customization_args'], {})

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 32)
        self.assertEqual(
            question_data['interaction']['customization_args'],
            {
                'buttonText': {
                    'value': 'Add item'
                }
            }
        )

    def test_question_state_dict_conversion_from_v32_to_v33(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        question_data['interaction']['id'] = 'MultipleChoiceInput'

        test_value = {
            'state': question_data,
            'state_schema_version': 32
        }

        self.assertEqual(
            question_data['interaction']['customization_args'], {})

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 33)
        self.assertEqual(
            question_data['interaction']['customization_args'],
            {
                'showChoicesInShuffledOrder': {
                    'value': True
                }
            }
        )

    def test_question_state_dict_conversion_from_v33_to_v34(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        question_data['content']['html'] = '<br/>'
        question_data['interaction']['default_outcome'][
            'feedback']['html'] = '<br/>'

        test_value = {
            'state': question_data,
            'state_schema_version': 33
        }

        self.assertEqual(
            test_value['state']['content']['html'], '<br/>')
        self.assertEqual(
            test_value['state']['interaction']['default_outcome'][
                'feedback']['html'],
            '<br/>'
        )

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 34)
        self.assertEqual(
            test_value['state']['content']['html'], '<br>')
        self.assertEqual(
            test_value['state']['interaction']['default_outcome'][
                'feedback']['html'],
            '<br>'
        )

    def test_question_state_dict_conversion_from_v34_to_v35(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        question_data['interaction']['id'] = 'MathExpressionInput'
        question_data['interaction']['solution'] = {
            'answer_is_exclusive': False,
            'correct_answer': {
                'ascii': '1'
            },
            'explanation': {
                'content_id': 'temp_id',
                'html': '<p>This is a solution.</p>'
            }
        }
        question_data['interaction']['answer_groups'] = [
            {
                'rule_specs': [{
                    'inputs': {
                        'x': '1',
                        'y': None
                    },
                    'rule_type': None
                }],
                'outcome': {
                    'feedback': {
                        'content_id': 'temp_id'
                    }
                },
            },
            {
                'rule_specs': [{
                    'inputs': {
                        'x': 'x+1',
                        'y': None
                    },
                    'rule_type': None
                }],
                'outcome': {
                    'feedback': {
                        'content_id': 'temp_id_2'
                    }
                },
            },
            {
                'rule_specs': [{
                    'inputs': {
                        'x': 'x=1',
                        'y': None
                    },
                    'rule_type': None
                }],
                'outcome': {
                    'feedback': {
                        'content_id': 'temp_id_3'
                    }
                },
            },
            {
                'rule_specs': [],
                'outcome': {
                    'feedback': {
                        'content_id': 'temp_id_4'
                    }
                },
            }
        ]
        question_data['recorded_voiceovers']['voiceovers_mapping'] = {
            'temp_id': {}, 'temp_id_2': {}, 'temp_id_3': {}, 'temp_id_4': {}
        }
        question_data['written_translations']['translations_mapping'] = {
            'temp_id': {}, 'temp_id_2': {}, 'temp_id_3': {}, 'temp_id_4': {}
        }

        test_value = {
            'state': question_data,
            'state_schema_version': 34
        }

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 35)
        self.assertEqual(
            test_value['state']['interaction']['id'],
            'MathEquationInput'
        )
        self.assertEqual(
            test_value['state']['recorded_voiceovers'][
                'voiceovers_mapping'],
            {'temp_id_3': {}}
        )
        self.assertEqual(
           test_value['state']['written_translations'][
               'translations_mapping'],
            {'temp_id_3': {}}
        )
        self.assertEqual(
            test_value['state']['interaction']['answer_groups'][0][
                'rule_specs'][0]['inputs']['y'],
            'both'
        )
        self.assertEqual(
            test_value['state']['interaction']['answer_groups'][0][
                'rule_specs'][0]['rule_type'],
            'MatchesExactlyWith'
        )
        self.assertEqual(
            test_value['state']['interaction']['answer_groups'][0][
                'outcome']['feedback']['content_id'],
            'temp_id_3'
        )
        self.assertNotIn(
            'ascii',
            test_value['state']['interaction']['solution']['correct_answer']
        )

        # Testing with only AlgebraicExpressionInput i.e ('x': 'x+1').
        test_value['state']['interaction']['id'] = 'MathExpressionInput'
        test_value['state']['interaction']['solution'] = {
            'answer_is_exclusive': False,
            'correct_answer': {
                'ascii': '1'
            },
            'explanation': {
                'content_id': 'temp_id',
                'html': '<p>This is a solution.</p>'
            }
        }
        test_value['state']['interaction']['answer_groups'] = [
            {
                'rule_specs': [{
                    'inputs': {
                        'x': 'x+1',
                        'y': None
                    },
                    'rule_type': None
                }],
                'outcome': {
                    'feedback': {
                        'content_id': 'temp_id'
                    }
                },
            }
        ]
        test_value['state']['recorded_voiceovers']['voiceovers_mapping'] = {
            'temp_id': {}
        }
        test_value['state']['written_translations']['translations_mapping'] = {
            'temp_id': {}
        }
        test_value['state_schema_version'] = 34

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 35)
        self.assertEqual(
            test_value['state']['interaction']['id'],
            'AlgebraicExpressionInput'
        )
        self.assertNotIn(
            'ascii',
            test_value['state']['interaction']['solution']['correct_answer']
        )
        self.assertEqual(
            test_value['state']['interaction']['answer_groups'][0][
                'rule_specs'][0]['rule_type'],
            'MatchesExactlyWith'
        )

        # Testing with only NumericExpressionInput i.e ('x': '1').
        test_value['state']['interaction']['id'] = 'MathExpressionInput'
        test_value['state']['interaction']['solution'] = {
            'answer_is_exclusive': False,
            'correct_answer': {
                'ascii': '1'
            },
            'explanation': {
                'content_id': 'temp_id',
                'html': '<p>This is a solution.</p>'
            }
        }
        test_value['state']['interaction']['answer_groups'] = [
            {
                'rule_specs': [{
                    'inputs': {
                        'x': '1',
                        'y': None
                    },
                    'rule_type': None
                }],
                'outcome': {
                    'feedback': {
                        'content_id': 'temp_id'
                    }
                },
            }
        ]
        test_value['state']['recorded_voiceovers']['voiceovers_mapping'] = {
            'temp_id': {}
        }
        test_value['state']['written_translations']['translations_mapping'] = {
            'temp_id': {}
        }
        test_value['state_schema_version'] = 34

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 35)
        self.assertEqual(
            test_value['state']['interaction']['id'],
            'NumericExpressionInput'
        )
        self.assertNotIn(
            'ascii',
            test_value['state']['interaction']['solution']['correct_answer']
        )
        self.assertEqual(
            test_value['state']['interaction']['answer_groups'][0][
                'rule_specs'][0]['rule_type'],
            'MatchesExactlyWith'
        )

    def test_question_state_dict_conversion_from_v35_to_v36(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        question_data['written_translations']['translations_mapping'] = {
            'temp_id_1': {
                'en': {
                    'html': 'html_body_1'
                }
            },
            'temp_id_2': {
                'en': {
                    'html': 'html_body_2'
                }
            }
        }

        test_value = {
            'state': question_data,
            'state_schema_version': 35
        }

        self.assertEqual(test_value['state']['next_content_id_index'], 0)

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 36)
        self.assertEqual(test_value['state']['next_content_id_index'], 3)

        t_map = test_value['state']['written_translations'][
            'translations_mapping']
        self.assertEqual(t_map['temp_id_1']['en']['data_format'], 'html')
        self.assertEqual(t_map['temp_id_2']['en']['data_format'], 'html')
        self.assertEqual(
            t_map['temp_id_1']['en']['translation'], 'html_body_1')
        self.assertEqual(
            t_map['temp_id_2']['en']['translation'], 'html_body_2')
        self.assertNotIn('html', t_map['temp_id_1']['en'])
        self.assertNotIn('html', t_map['temp_id_2']['en'])

        # Testing with interaction id 'PencilCodeEditor'.
        test_value['state']['interaction']['id'] = 'PencilCodeEditor'
        test_value['state']['interaction']['customization_args'] = {
            'initial_code': {}
        }
        test_value['state']['written_translations']['translations_mapping'] = {
            'temp_id_1': {
                'en': {
                    'html': 'html_body_1'
                }
            },
            'temp_id_2': {
                'en': {
                    'html': 'html_body_2'
                }
            }
        }
        test_value['state_schema_version'] = 35

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 36)
        self.assertEqual(
            test_value['state']['interaction']['customization_args'],
            {'initialCode': {}}
        )
        self.assertEqual(
            test_value['state']['written_translations']['translations_mapping'],
            {
                'temp_id_1': {
                    'en': {'data_format': 'html', 'translation': 'html_body_1'}
                },
                'temp_id_2': {
                    'en': {'data_format': 'html', 'translation': 'html_body_2'}
                }
            }
        )

        # Testing with interaction id 'TextInput'.
        test_value['state']['interaction']['id'] = 'TextInput'
        test_value['state']['interaction']['customization_args'] = {
            'placeholder': {
                'value': 'temp_value_1'
            }
        }
        test_value['state']['written_translations']['translations_mapping'] = {
            'temp_id_1': {
                'en': {
                    'html': 'html_body_1'
                }
            },
            'temp_id_2': {
                'en': {
                    'html': 'html_body_2'
                }
            }
        }
        test_value['state_schema_version'] = 35

        with self.swap_to_always_return(
            customization_args_util, 'validate_customization_args_and_values',
            value=True):
            question_domain.Question.update_state_from_model(
                test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 36)

        # Testing with interaction id 'MultipleChoiceInput'.
        test_value['state']['interaction']['id'] = 'MultipleChoiceInput'
        test_value['state']['interaction']['customization_args'] = {
            'choices': {
                'value': 'value_1'
            }
        }
        test_value['state']['written_translations']['translations_mapping'] = {
            'temp_id_1': {
                'en': {
                    'html': 'html_body_1'
                }
            },
            'temp_id_2': {
                'en': {
                    'html': 'html_body_2'
                }
            }
        }
        test_value['state']['recorded_voiceovers']['voiceovers_mapping'] = {}
        test_value['state_schema_version'] = 35

        with self.swap_to_always_return(
            customization_args_util, 'validate_customization_args_and_values',
            value=True):
            question_domain.Question.update_state_from_model(
                test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 36)
        self.assertEqual(
            test_value['state']['interaction']['customization_args'],
            {
                'choices': {
                    'value': [
                        {'content_id': 'ca_choices_3', 'html': 'v'},
                        {'content_id': 'ca_choices_4', 'html': 'a'},
                        {'content_id': 'ca_choices_5', 'html': 'l'},
                        {'content_id': 'ca_choices_6', 'html': 'u'},
                        {'content_id': 'ca_choices_7', 'html': 'e'},
                        {'content_id': 'ca_choices_8', 'html': '_'},
                        {'content_id': 'ca_choices_9', 'html': '1'}
                    ]
                },
                'showChoicesInShuffledOrder': {'value': True}
            }
        )
        self.assertEqual(
            test_value['state']['recorded_voiceovers']['voiceovers_mapping'],
            {
                'ca_choices_3': {}, 'ca_choices_4': {}, 'ca_choices_5': {},
                'ca_choices_6': {}, 'ca_choices_7': {}, 'ca_choices_8': {},
                'ca_choices_9': {}
            }
        )
        self.assertEqual(
            test_value['state']['written_translations']['translations_mapping'],
            {
                'temp_id_1': {
                    'en': {'data_format': 'html', 'translation': 'html_body_1'}
                },
                'temp_id_2': {
                    'en': {'data_format': 'html', 'translation': 'html_body_2'}
                },
                'ca_choices_3': {}, 'ca_choices_4': {}, 'ca_choices_5': {},
                'ca_choices_6': {}, 'ca_choices_7': {}, 'ca_choices_8': {},
                'ca_choices_9': {}
            }
        )

        # Testing with interaction id 'ItemSelectionInput'.
        test_value['state']['interaction']['id'] = 'ItemSelectionInput'
        test_value['state']['interaction']['customization_args'] = {}
        test_value['state']['written_translations']['translations_mapping'] = {
            'temp_id_1': {
                'en': {
                    'html': 'html_body_1'
                }
            },
            'temp_id_2': {
                'en': {
                    'html': 'html_body_2'
                }
            }
        }
        test_value['state']['recorded_voiceovers']['voiceovers_mapping'] = {}
        test_value['state_schema_version'] = 35

        self.assertEqual(
            test_value['state']['interaction']['customization_args'], {}
        )

        with self.swap_to_always_return(
            customization_args_util, 'validate_customization_args_and_values',
            value=True):
            question_domain.Question.update_state_from_model(
                test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 36)
        self.assertEqual(
            test_value['state']['interaction']['customization_args'],
            {
                'choices': {
                    'value': [{'content_id': 'ca_choices_3', 'html': ''}]
                },
                'maxAllowableSelectionCount': {'value': 1},
                'minAllowableSelectionCount': {'value': 1}
            }
        )
        self.assertEqual(
            test_value['state']['recorded_voiceovers']['voiceovers_mapping'],
            {'ca_choices_3': {}}
        )
        self.assertEqual(
            test_value['state']['written_translations']['translations_mapping'],
            {
                'temp_id_1': {
                    'en': {'data_format': 'html', 'translation': 'html_body_1'}
                },
                'temp_id_2': {
                    'en': {'data_format': 'html', 'translation': 'html_body_2'}
                },
                'ca_choices_3': {}
            }
        )

    def test_question_state_dict_conversion_from_v36_to_v37(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        question_data['interaction']['id'] = 'TextInput'
        question_data['interaction']['answer_groups'] = [{
            'rule_specs': [{
                'rule_type': 'CaseSensitiveEquals'
            }]
        }]

        test_value = {
            'state': question_data,
            'state_schema_version': 36
        }

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 37)
        self.assertEqual(
            test_value['state']['interaction']['answer_groups'][0][
                'rule_specs'][0]['rule_type'],
            'Equals'
        )

    def test_question_state_dict_conversion_from_v37_to_v38(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        question_data['interaction']['id'] = 'MathEquationInput'
        question_data['interaction']['answer_groups'] = [{
            'rule_specs': [{
                'inputs': {
                    'x': 'variable=pi'
                }
            }]
        }]
        question_data['interaction']['customization_args'] = {}

        test_value = {
            'state': question_data,
            'state_schema_version': 37
        }

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 38)
        self.assertEqual(
            question_data['interaction']['customization_args'],
            {
                'customOskLetters': {
                    'value': ['a', 'b', 'e', 'i', 'l', 'r', 'v', 'π']
                }
            }
        )

    def test_question_state_dict_conversion_from_v38_to_v39(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        question_data['interaction']['id'] = 'NumericExpressionInput'
        question_data['interaction']['customization_args'] = {}
        question_data['recorded_voiceovers']['voiceovers_mapping'] = {}
        question_data['written_translations']['translations_mapping'] = {}

        test_value = {
            'state': question_data,
            'state_schema_version': 38
        }

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 39)
        self.assertEqual(
            test_value['state']['interaction']['customization_args'],
            {
                'placeholder': {
                    'value': {
                        'content_id': 'ca_placeholder_0',
                        'unicode_str': (
                            'Type an expression here, using only numbers.')
                    }
                }
            }
        )
        self.assertEqual(
            test_value['state']['recorded_voiceovers']['voiceovers_mapping'],
            {'ca_placeholder_0': {}}
        )
        self.assertEqual(
            test_value['state']['written_translations']['translations_mapping'],
            {'ca_placeholder_0': {}}
        )

    def test_question_state_dict_conversion_from_v39_to_v40(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        question_data['interaction']['id'] = 'TextInput'
        question_data['interaction']['answer_groups'] = [{
            'rule_specs': [{
                'inputs': {
                    'x': 'variable=pi'
                },
                'rule_type': 'standard'
            }]
        }]

        test_value = {
            'state': question_data,
            'state_schema_version': 39
        }

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 40)
        self.assertEqual(
            test_value['state']['interaction']['answer_groups'][0][
                'rule_specs'][0],
            {
                'rule_type': 'standard',
                'inputs': {'x': ['variable=pi']}
            }
        )

    def test_question_state_dict_conversion_from_v40_to_v41(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        question_data['interaction']['id'] = 'TextInput'
        question_data['interaction']['answer_groups'] = [{
            'rule_specs': [{
                'rule_type': 'standard',
                'inputs': {
                    'x': 'text'
                },
            }]
        }]
        question_data['next_content_id_index'] = 0
        question_data['recorded_voiceovers']['voiceovers_mapping'] = {}
        question_data['written_translations']['translations_mapping'] = {}

        test_value = {
            'state': question_data,
            'state_schema_version': 40
        }

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 41)
        self.assertEqual(test_value['state']['next_content_id_index'], 1)
        self.assertEqual(
            test_value['state']['interaction']['answer_groups'][0][
                'rule_specs'][0]['inputs']['x'],
            {
                'contentId': 'rule_input_0',
                'normalizedStrSet': 'text'
            }
        )
        self.assertEqual(
            test_value['state']['recorded_voiceovers']['voiceovers_mapping'],
            {'rule_input_0': {}}
        )
        self.assertEqual(
            test_value['state']['written_translations']['translations_mapping'],
            {'rule_input_0': {}}
        )

        # Testing with interaction id 'SetInput'.
        test_value['state']['interaction']['id'] = 'SetInput'
        test_value['state']['interaction']['answer_groups'] = [{
            'rule_specs': [{
                'rule_type': 'standard',
                'inputs': {
                    'x': 'text'
                },
            }]
        }]
        test_value['state']['next_content_id_index'] = 0
        test_value['state']['recorded_voiceovers']['voiceovers_mapping'] = {}
        test_value['state']['written_translations']['translations_mapping'] = {}
        test_value['state_schema_version'] = 40

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 41)
        self.assertEqual(test_value['state']['next_content_id_index'], 1)
        self.assertEqual(
            test_value['state']['interaction']['answer_groups'][0][
                'rule_specs'][0]['inputs']['x'],
            {
                'contentId': 'rule_input_0',
                'unicodeStrSet': 'text'
            }
        )
        self.assertEqual(
            test_value['state']['recorded_voiceovers']['voiceovers_mapping'],
            {'rule_input_0': {}}
        )
        self.assertEqual(
            test_value['state']['written_translations']['translations_mapping'],
            {'rule_input_0': {}}
        )

    def test_question_state_dict_conversion_from_v41_to_v42(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        question_data['interaction']['id'] = 'ItemSelectionInput'
        question_data['interaction']['solution'] = {
            'correct_answer': ['correct_value']
        }
        question_data['interaction']['customization_args'] = {
            'choices': {
                'value': [
                    {'html': 'correct_value', 'content_id': 'content_id_1'},
                    {'html': 'value_2', 'content_id': 'content_id_2'},
                    {'html': 'value_3', 'content_id': 'content_id_3'}
                ]
            }
        }
        question_data['interaction']['answer_groups'] = [{
            'rule_specs': [{
                'inputs': {
                    'x': ['correct_value'],
                },
                'rule_type': 'IsEqualToOrdering'
            }]
        }]

        test_value = {
            'state': question_data,
            'state_schema_version': 41
        }

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 42)
        self.assertEqual(
            test_value['state']['interaction']['answer_groups'][0][
                'rule_specs'][0]['inputs']['x'],
            ['content_id_1']
        )
        self.assertEqual(
            test_value['state']['interaction']['solution'],
            {'correct_answer': ['content_id_1']}
        )

        # Testing with invalid 'x' input.
        test_value['state']['interaction']['id'] = 'ItemSelectionInput'
        test_value['state']['interaction']['solution'] = {
            'correct_answer': ['correct_value']
        }
        test_value['state']['interaction']['customization_args'] = {
            'choices': {
                'value': [
                    {'html': 'correct_value', 'content_id': 'content_id_1'},
                ]
            }
        }
        test_value['state']['interaction']['answer_groups'] = [{
            'rule_specs': [{
                'inputs': {
                    'x': ['invalid_value'],
                },
                'rule_type': 'IsEqualToOrdering'
            }]
        }]
        test_value['state_schema_version'] = 41

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 42)
        self.assertEqual(
            test_value['state']['interaction']['answer_groups'][0][
                'rule_specs'][0]['inputs']['x'],
            ['invalid_content_id']
        )
        self.assertEqual(
            test_value['state']['interaction']['solution'],
            {'correct_answer': ['content_id_1']}
        )

        # Testing with interaction id 'DragAndDropSortInput'.
        test_value['state']['interaction']['id'] = 'DragAndDropSortInput'
        test_value['state']['interaction']['solution'] = {
            'correct_answer': [['correct_value']]
        }
        test_value['state']['interaction']['customization_args'] = {
            'choices': {
                'value': [
                    {'html': 'correct_value', 'content_id': 'content_id_1'},
                    {'html': 'value_2', 'content_id': 'content_id_2'},
                    {'html': 'value_3', 'content_id': 'content_id_3'}
                ]
            }
        }
        test_value['state']['interaction']['answer_groups'] = [{
            'rule_specs': [
                {
                    'inputs': {
                        'x': [['value_2']],
                    },
                    'rule_type': 'IsEqualToOrdering'
                },
                {
                    'inputs': {
                        'x': 'correct_value',
                    },
                    'rule_type': 'HasElementXAtPositionY'
                },
                {
                    'inputs': {
                        'x': 'correct_value',
                        'y': 'value_3'
                    },
                    'rule_type': 'HasElementXBeforeElementY'
                }
            ]
        }]
        test_value['state_schema_version'] = 41

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 42)
        self.assertEqual(
            test_value['state']['interaction']['answer_groups'][0],
            {
                'rule_specs': [
                    {
                        'inputs': {
                            'x': [['content_id_2']]
                        },
                        'rule_type': 'IsEqualToOrdering'
                    },
                    {
                        'inputs': {'x': 'content_id_1'},
                        'rule_type': 'HasElementXAtPositionY'
                    },
                    {
                        'inputs': {
                            'x': 'content_id_1',
                            'y': 'content_id_3'
                        },
                        'rule_type': 'HasElementXBeforeElementY'
                    }
                ]
            }
        )
        self.assertEqual(
            test_value['state']['interaction']['solution'],
            {'correct_answer': [['content_id_1']]}
        )

    def test_question_state_dict_conversion_from_v42_to_v43(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        question_data['interaction']['id'] = 'NumericExpressionInput'

        test_value = {
            'state': question_data,
            'state_schema_version': 42
        }

        self.assertEqual(
            test_value['state']['interaction']['customization_args'],
            {}
        )

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 43)
        self.assertEqual(
            test_value['state']['interaction']['customization_args'],
            {
                'useFractionForDivision': {
                    'value': True
                }
            }
        )

    def test_question_state_dict_conversion_from_v43_to_v44(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())
        del question_data['card_is_checkpoint']

        test_value = {
            'state': question_data,
            'state_schema_version': 43
        }

        self.assertNotIn('card_is_checkpoint', test_value['state'])

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 44)
        self.assertEqual(test_value['state']['card_is_checkpoint'], False)

    def test_question_state_dict_conversion_from_v44_to_v45(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())
        del question_data['linked_skill_id']

        test_value = {
            'state': question_data,
            'state_schema_version': 44
        }

        self.assertNotIn('linked_skill_id', test_value['state'])

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 45)
        self.assertIsNone(test_value['state']['linked_skill_id'])

    def test_question_state_dict_conversion_from_v45_to_v46(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        test_value = {
            'state': question_data,
            'state_schema_version': 45
        }

        initial_json = copy.deepcopy(test_value['state'])

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 46)
        self.assertEqual(test_value['state'], initial_json)

    def test_question_state_dict_conversion_from_v46_to_v47(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        question_data['content']['html'] = (
            '<oppia-noninteractive-svgdiagram '
            'svg_filename-with-value="filename.svg">'
            '</oppia-noninteractive-svgdiagram>'
        )

        test_value = {
            'state': question_data,
            'state_schema_version': 46
        }

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 47)
        self.assertEqual(
            test_value['state']['content']['html'],
            '<oppia-noninteractive-image '
            'caption-with-value="&amp;quot;&amp;quot;" '
            'filepath-with-value="filename.svg">'
            '</oppia-noninteractive-image>'
        )

    def test_question_state_dict_conversion_from_v47_to_v48(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        question_data['content']['html'] = '&nbsp;'

        test_value = {
            'state': question_data,
            'state_schema_version': 47
        }

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 48)
        self.assertEqual(test_value['state']['content']['html'], ' ')

    def test_question_state_dict_conversion_from_v48_to_v49(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        question_data['interaction']['id'] = 'NumericInput'

        test_value = {
            'state': question_data,
            'state_schema_version': 48
        }

        self.assertEqual(
            test_value['state']['interaction']['customization_args'],
            {}
        )

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 49)
        self.assertEqual(
            test_value['state']['interaction']['customization_args'],
            {
                'requireNonnegativeInput': {
                    'value': False
                }
            }
        )

    def test_question_state_dict_conversion_from_v49_to_v50(self):
        question_data = (
            question_domain.Question.create_default_question_state().to_dict())

        question_data['interaction']['id'] = 'AlgebraicExpressionInput'
        question_data['interaction']['customization_args'] = {
            'customOskLetters': ['a', 'b', 'c']
        }
        question_data['interaction']['answer_groups'] = [{
            'outcome': {
                'dest': 'abc',
                'feedback': {
                    'content_id': 'feedback_2',
                    'html': '<p>Feedback</p>'
                },
                'labelled_as_correct': True,
                'param_changes': [],
                'refresher_exploration_id': None,
                'missing_prerequisite_skill_id': None
            },
            'rule_specs': [{
                'inputs': {
                    'x': 'a - b'
                },
                'rule_type': 'ContainsSomeOf'
            }, {
                'inputs': {
                    'x': 'a - b',
                    'y': []
                },
                'rule_type': 'MatchesExactlyWith'
            }],
            'training_data': [],
            'tagged_skill_misconception_id': None
        }]

        test_value = {
            'state': question_data,
            'state_schema_version': 49
        }

        question_domain.Question.update_state_from_model(
            test_value, test_value['state_schema_version'])

        self.assertEqual(test_value['state_schema_version'], 50)

        rule_specs = test_value[
            'state']['interaction']['answer_groups'][0]['rule_specs']
        self.assertEqual(len(rule_specs), 1)
        self.assertEqual(rule_specs[0]['rule_type'], 'MatchesExactlyWith')
        self.assertEqual(
            test_value['state']['interaction']['customization_args'], {
                'allowedVariables': ['a', 'b', 'c']
            }
        )

    def test_get_all_translatable_content_for_question(self):
        """Get all translatable fields from exploration."""
        translatable_contents = [
            translatable_content.content_value
            for translatable_content in
            self.question.get_all_contents_which_need_translations(
                self.dummy_entity_translations)
        ]

        self.assertItemsEqual(
            translatable_contents,
            [
                'Enter text here',
                '<p>This is a hint.</p>',
                '<p>This is a solution.</p>'
            ])


class QuestionSummaryTest(test_utils.GenericTestBase):
    """Test for Question Summary object."""

    def setUp(self):
        super(QuestionSummaryTest, self).setUp()
        self.fake_date_created = datetime.datetime(
            2018, 11, 17, 20, 2, 45, 0)
        self.fake_date_updated = datetime.datetime(
            2018, 11, 17, 20, 3, 14, 0)
        self.observed_object = question_domain.QuestionSummary(
            question_id='question_1',
            question_content='<p>question content</p>',
            interaction_id='TextInput',
            question_model_created_on=self.fake_date_created,
            question_model_last_updated=self.fake_date_updated,
            misconception_ids=['skill1-1', 'skill2-2']
        )

    def test_to_dict(self):
        """Test to verify to_dict method of the Question Summary
        object.
        """
        expected_object_dict = {
            'id': 'question_1',
            'question_content': '<p>question content</p>',
            'interaction_id': 'TextInput',
            'last_updated_msec': utils.get_time_in_millisecs(
                self.fake_date_updated),
            'created_on_msec': utils.get_time_in_millisecs(
                self.fake_date_created),
            'misconception_ids': ['skill1-1', 'skill2-2']
        }

        self.assertEqual(expected_object_dict, self.observed_object.to_dict())

    def test_validation_with_valid_properties(self):
        self.observed_object.validate()

    def test_validation_with_invalid_id(self):
        self.observed_object.id = 1
        with self.assertRaisesRegex(
            utils.ValidationError, 'Expected id to be a string, received 1'):
            self.observed_object.validate()

    def test_validation_with_invalid_interaction_id(self):
        self.observed_object.interaction_id = 1
        with self.assertRaisesRegex(
            utils.ValidationError,
            'Expected interaction id to be a string, received 1'):
            self.observed_object.validate()

    def test_validation_with_invalid_question_content(self):
        self.observed_object.question_content = 1
        with self.assertRaisesRegex(
            utils.ValidationError,
            'Expected question content to be a string, received 1'):
            self.observed_object.validate()

    def test_validation_with_invalid_created_on(self):
        self.observed_object.created_on = 1
        with self.assertRaisesRegex(
            utils.ValidationError,
            'Expected created on to be a datetime, received 1'):
            self.observed_object.validate()

    def test_validation_with_invalid_last_updated(self):
        self.observed_object.last_updated = 1
        with self.assertRaisesRegex(
            utils.ValidationError,
            'Expected last updated to be a datetime, received 1'):
            self.observed_object.validate()

    def test_validate_invalid_list_of_misconception_ids(self):
        """Test to verify that the validation fails when
        misconception_ids value is an invalid list.
        """
        self.observed_object.misconception_ids = ['Test', 1]
        with self.assertRaisesRegex(
            utils.ValidationError,
            re.escape(
                'Expected misconception ids to be a list of strings, '
                'received [\'Test\', 1]')):
            self.observed_object.validate()

    def test_validate_invalid_type_of_misconception_ids(self):
        """Test to verify that the validation fails when
        misconception_ids value is an invalid type.
        """
        self.observed_object.misconception_ids = 123
        with self.assertRaisesRegex(
            utils.ValidationError,
            'Expected misconception ids to be a list of strings, '
            'received 123'):
            self.observed_object.validate()


class QuestionSkillLinkDomainTest(test_utils.GenericTestBase):
    """Test for Question Skill Link Domain object."""

    def test_to_dict(self):
        """Test to verify to_dict method of the Question Skill Link Domain
        object.
        """
        expected_object_dict = {
            'question_id': 'testquestion',
            'skill_id': 'testskill',
            'skill_description': 'testskilldescription',
            'skill_difficulty': 0.5,
        }
        observed_object = question_domain.QuestionSkillLink(
            'testquestion', 'testskill', 'testskilldescription', 0.5)
        self.assertEqual(expected_object_dict, observed_object.to_dict())


class MergedQuestionSkillLinkDomainTest(test_utils.GenericTestBase):
    """Test for Merged Question Skill Link Domain object."""

    def test_to_dict(self):
        """Test to verify to_dict method of the Merged Question Skill Link
        Domain object.
        """
        expected_object_dict = {
            'question_id': 'testquestion',
            'skill_ids': ['testskill'],
            'skill_descriptions': ['testskilldescription'],
            'skill_difficulties': [0.5],
        }
        observed_object = question_domain.MergedQuestionSkillLink(
            'testquestion', ['testskill'], ['testskilldescription'], [0.5])
        self.assertEqual(expected_object_dict, observed_object.to_dict())
