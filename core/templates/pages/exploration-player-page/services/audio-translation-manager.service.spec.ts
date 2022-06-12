// Copyright 2018 The Oppia Authors. All Rights Reserved.
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
 * @fileoverview Unit tests for the audio translation manager service.
 */

import { TestBed } from '@angular/core/testing';
import { Voiceover } from 'domain/exploration/voiceover.model';

import { AudioTranslationManagerService, AudioTranslations } from
  'pages/exploration-player-page/services/audio-translation-manager.service';

describe('Audio translation manager service', () => {
  let atms: AudioTranslationManagerService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [AudioTranslationManagerService]
    });

    atms = TestBed.get(AudioTranslationManagerService);
  });

  var testAudioTranslations: AudioTranslations;
  var testAudioTranslations2: AudioTranslations;
  beforeEach(() => {
    testAudioTranslations = {
      en: Voiceover.createFromBackendDict({
        filename: 'audio-en.mp3',
        file_size_bytes: 0.5,
        needs_update: false,
        duration_secs: 0.5
      }),
      es: Voiceover.createFromBackendDict({
        filename: 'audio-es.mp3',
        file_size_bytes: 0.5,
        needs_update: false,
        duration_secs: 0.5
      })
    };

    testAudioTranslations2 = {
      zh: Voiceover.createFromBackendDict({
        filename: 'audio-zh.mp3',
        file_size_bytes: 0.5,
        needs_update: false,
        duration_secs: 0.5
      }),
      'hi-en': Voiceover.createFromBackendDict({
        filename: 'audio-hi-en.mp3',
        file_size_bytes: 0.5,
        needs_update: false,
        duration_secs: 0.5
      })
    };
  });

  it('should properly set primary, secondary and sequential audio translations',
    () => {
      atms.setContentAudioTranslations(testAudioTranslations, '', '');
      expect(atms.getCurrentAudioTranslations()).toEqual({
        en: Voiceover.createFromBackendDict({
          filename: 'audio-en.mp3',
          file_size_bytes: 0.5,
          needs_update: false,
          duration_secs: 0.5
        }),
        es: Voiceover.createFromBackendDict({
          filename: 'audio-es.mp3',
          file_size_bytes: 0.5,
          needs_update: false,
          duration_secs: 0.5
        })
      });
      atms.setSecondaryAudioTranslations(testAudioTranslations2, '', '');
      expect(atms.getCurrentAudioTranslations()).toEqual({
        zh: Voiceover.createFromBackendDict({
          filename: 'audio-zh.mp3',
          file_size_bytes: 0.5,
          needs_update: false,
          duration_secs: 0.5
        }),
        'hi-en': Voiceover.createFromBackendDict({
          filename: 'audio-hi-en.mp3',
          file_size_bytes: 0.5,
          needs_update: false,
          duration_secs: 0.5
        })
      });
      atms.clearSecondaryAudioTranslations();
      expect(atms.getCurrentAudioTranslations()).toEqual({
        en: Voiceover.createFromBackendDict({
          filename: 'audio-en.mp3',
          file_size_bytes: 0.5,
          needs_update: false,
          duration_secs: 0.5
        }),
        es: Voiceover.createFromBackendDict({
          filename: 'audio-es.mp3',
          file_size_bytes: 0.5,
          needs_update: false,
          duration_secs: 0.5
        })
      });
      atms.setSequentialAudioTranslations(
        testAudioTranslations, '<p>test</p>', '');
      expect(atms.getCurrentHtmlForAutogeneratedSequentialAudio())
        .toEqual('<p>test</p>');
    });

  it('should properly get html for autogenerated audio',
    () => {
      const _contentHtmlForAutogeneratedAudio =
      '<p>contentHtmlForAutogeneratedAudio</p>';
      const _secondaryHtmlForAutogeneratedAudio =
      '<p>secondaryHtmlForAutogeneratedAudio</p>';
      atms.setContentAudioTranslations(
        testAudioTranslations, _contentHtmlForAutogeneratedAudio, '');
      expect(atms.getCurrentHtmlForAutogeneratedAudio()).toEqual(
        _contentHtmlForAutogeneratedAudio
      );
      atms.setSecondaryAudioTranslations(
        testAudioTranslations2, _secondaryHtmlForAutogeneratedAudio, '');
      expect(atms.getCurrentHtmlForAutogeneratedAudio()).toEqual(
        _secondaryHtmlForAutogeneratedAudio
      );
    });

  it('should properly get component name',
    () => {
      const _contentComponentName =
      '<p>contentComponentName</p>';
      const _secondaryComponentName =
      '<p>secondaryComponentName</p>';
      atms.setContentAudioTranslations(
        testAudioTranslations, '', _contentComponentName);
      expect(atms.getCurrentComponentName()).toEqual(
        _contentComponentName
      );
      atms.setSecondaryAudioTranslations(
        testAudioTranslations2, '', _secondaryComponentName);
      expect(atms.getCurrentComponentName()).toEqual(
        _secondaryComponentName
      );
    });
});
