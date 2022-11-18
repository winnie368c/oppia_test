// Copyright 2017 The Oppia Authors. All Rights Reserved.
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
 * @fileoverview Unit tests to operate the playback of autogenerated audio
 * using the SpeechSynthesis API.
 */

import { async, TestBed } from '@angular/core/testing';
import { AutogeneratedAudioPlayerService } from './autogenerated-audio-player.service';
import { ContextService } from './context.service';
import { SpeechSynthesisChunkerService } from './speech-synthesis-chunker.service';

describe('BannerComponent', () => {
  let autogeneratedAudioPlayerService: AutogeneratedAudioPlayerService;
  let speechSynthesisChunkerService: SpeechSynthesisChunkerService;
  let contextService: ContextService;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      providers: [
        AutogeneratedAudioPlayerService,
        SpeechSynthesisChunkerService,
        ContextService
      ]
    });
    speechSynthesisChunkerService =
      TestBed.inject(SpeechSynthesisChunkerService);
    contextService = TestBed.inject(ContextService);
  }));

  describe('if the audio is not playing', () => {
    beforeEach(() => {
      spyOnProperty(window, 'speechSynthesis').and
        .returnValue({speaking: false});
      autogeneratedAudioPlayerService =
        TestBed.inject(AutogeneratedAudioPlayerService);
      spyOn(contextService, 'getExplorationId').and.returnValue('exp1');
    });

    it('should return void when utterance is null', () => {
      spyOn(autogeneratedAudioPlayerService, '_play').and.callThrough();
      spyOn(speechSynthesisChunkerService, 'speak').and.callFake((
          utterance, audioFinishedCallback: Function) => {
        audioFinishedCallback();
      });
      spyOn(speechSynthesisChunkerService, 'cancel');
      spyOn(speechSynthesisChunkerService, 'convertToSpeakableText');
      autogeneratedAudioPlayerService.utterance = null;

      autogeneratedAudioPlayerService.play(
        '<p>test text</p>', 'en-US', () => {}
      );

      expect(autogeneratedAudioPlayerService._play).toHaveBeenCalled();
      expect(speechSynthesisChunkerService.cancel).toHaveBeenCalled();
      expect(speechSynthesisChunkerService.convertToSpeakableText)
        .not.toHaveBeenCalled();
    });

    it('should start playing audio when play button is clicked', () => {
      spyOn(autogeneratedAudioPlayerService, '_play').and.callThrough();
      spyOn(speechSynthesisChunkerService, 'speak').and.callFake((
          utterance, audioFinishedCallback: Function) => {
        audioFinishedCallback();
      });
      spyOn(speechSynthesisChunkerService, 'cancel');

      autogeneratedAudioPlayerService.play(
        '<p>test text</p>', 'en-US', () => {}
      );

      expect(autogeneratedAudioPlayerService._play).toHaveBeenCalledWith(
        '<p>test text</p>', 'en-US', jasmine.any(Function)
      );
      expect(speechSynthesisChunkerService.cancel).toHaveBeenCalled();
      expect(autogeneratedAudioPlayerService.utterance)
        .toBeInstanceOf(SpeechSynthesisUtterance);
      // Value of utteance can be null or object of SpeechSynthesisUtterance,
      // so to prevent typescript strict check error
      // "object is possibly null" we imposed an if statement here.
      if (autogeneratedAudioPlayerService.utterance !== null) {
        expect(autogeneratedAudioPlayerService.utterance.text)
          .toBe('test text');
        expect(autogeneratedAudioPlayerService.utterance.lang).toBe('en-US');
        expect(autogeneratedAudioPlayerService.utterance.rate).toBeCloseTo(
          autogeneratedAudioPlayerService.DEFAULT_PLAYBACK_RATE
        );
        expect(autogeneratedAudioPlayerService.utterance.volume).toBe(
          autogeneratedAudioPlayerService.DEFAULT_PLAYBACK_VOLUME
        );
      }
      expect(speechSynthesisChunkerService.speak)
        .toHaveBeenCalledWith(
          autogeneratedAudioPlayerService.utterance, jasmine.any(Function)
        );
    });

    it('should stop playing audio when pause button is clicked', () => {
      spyOn(speechSynthesisChunkerService, 'cancel');

      autogeneratedAudioPlayerService.cancel();

      expect(speechSynthesisChunkerService.cancel).toHaveBeenCalled();
    });

    it('should return false if auto generated audio is not playing', () => {
      // Pre-checks.
      expect(autogeneratedAudioPlayerService._speechSynthesis).not.toBeNull();
      // Value of _speechSynthesis can be null or object of
      // window.speechSynthesis, so to prevent typescript strict check error
      // "object is possibly null" we imposed an if statement here.
      if (autogeneratedAudioPlayerService._speechSynthesis !== null) {
        expect(autogeneratedAudioPlayerService._speechSynthesis.speaking)
          .toBeFalse();
      }
      expect(autogeneratedAudioPlayerService.isPlaying()).toBeFalse();
    });
  });

  describe('if the audio is playing', () => {
    beforeEach(() => {
      spyOnProperty(window, 'speechSynthesis').and
        .returnValue({speaking: true});
      autogeneratedAudioPlayerService =
        TestBed.inject(AutogeneratedAudioPlayerService);
    });

    it('should return true if auto generated audio is playing', () => {
      // Pre-checks.
      expect(autogeneratedAudioPlayerService._speechSynthesis).not.toBeNull();
      // Value of _speechSynthesis can be null or object of
      // window.speechSynthesis, so to prevent typescript strict check error
      // "object is possibly null" we imposed an if statement here.
      if (autogeneratedAudioPlayerService._speechSynthesis !== null) {
        expect(autogeneratedAudioPlayerService._speechSynthesis.speaking)
          .toBeTrue();
      }
      expect(autogeneratedAudioPlayerService.isPlaying()).toBeTrue();
    });
  });
});
