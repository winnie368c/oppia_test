// Copyright 2021 The Oppia Authors. All Rights Reserved.
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
 * @fileoverview Component for an input/response pair in the learner view.
 */

import { Component, EventEmitter, Input, Output, ViewChild } from '@angular/core';
import { downgradeComponent } from '@angular/upgrade/static';
import { NgbPopover } from '@ng-bootstrap/ng-bootstrap';
import { AppConstants } from 'app.constants';
import { InputResponsePair } from 'domain/state_card/state-card.model';
import { InteractionSpecsConstants } from 'pages/interaction-specs.constants';
import { AudioPlayerService } from 'services/audio-player.service';
import { AutogeneratedAudioPlayerService } from 'services/autogenerated-audio-player.service';
import { ExplorationHtmlFormatterService } from 'services/exploration-html-formatter.service';
import { ExplorationPlayerConstants } from '../exploration-player-page.constants';
import { AudioTranslationManagerService } from '../services/audio-translation-manager.service';
import { PlayerPositionService } from '../services/player-position.service';
import { PlayerTranscriptService } from '../services/player-transcript.service';
import { I18nLanguageCodeService } from 'services/i18n-language-code.service';

@Component({
  selector: 'oppia-input-response-pair',
  templateUrl: './input-response-pair.component.html'
})
export class InputResponsePairComponent {
  @Input() data: InputResponsePair;
  @Output() dataChange: EventEmitter<InputResponsePair> = new EventEmitter();
  @Input() oppiaAvatarImageUrl: string;
  @Input() profilePicture: string;
  @Input() inputResponsePairId: string;
  @Input() isLastPair: boolean;
  OPPIA_AVATAR_LINK_URL: string;
  decodedProfilePicture: string;
  @ViewChild('popover') popover: NgbPopover;

  constructor(
    private audioPlayerService: AudioPlayerService,
    private audioTranslationManagerService: AudioTranslationManagerService,
    private autogeneratedAudioPlayerService: AutogeneratedAudioPlayerService,
    private explorationHtmlFormatterService: ExplorationHtmlFormatterService,
    private i18nLanguageCodeService: I18nLanguageCodeService,
    private playerPositionService: PlayerPositionService,
    private playerTranscriptService: PlayerTranscriptService,
  ) {}

  ngOnInit(): void {
    this.decodedProfilePicture = decodeURIComponent(this.profilePicture);
  }

  isVideoRteElementPresentInResponse(): boolean {
    return this.data.oppiaResponse.includes(
      'oppia-noninteractive-video');
  }

  isCurrentCardAtEndOfTranscript(): boolean {
    return this.playerTranscriptService.isLastCard(
      this.playerPositionService.getDisplayedCardIndex());
  }

  isLanguageRTL(): boolean {
    return this.i18nLanguageCodeService.isCurrentLanguageRTL();
  }

  getAnswerHtml(): string {
    let displayedCard = this.playerTranscriptService.getCard(
      this.playerPositionService.getDisplayedCardIndex());
    let interaction = displayedCard.getInteraction();
    if (this.data) {
      return this.explorationHtmlFormatterService.getAnswerHtml(
        this.data.learnerInput, interaction.id,
        interaction.customizationArgs);
    }
  }

  // Returns a HTML string representing a short summary of the answer
  // , or null if the answer does not have to be summarized.
  getShortAnswerHtml(): string {
    let displayedCard = this.playerTranscriptService.getCard(
      this.playerPositionService.getDisplayedCardIndex());
    let interaction = displayedCard.getInteraction();
    let shortAnswerHtml = '';
    if (this.data.learnerInput.hasOwnProperty('answerDetails')) {
      shortAnswerHtml = (
        this.data.learnerInput as unknown as { answerDetails: string })
        .answerDetails;
    } else if (
      this.data && interaction.id &&
        InteractionSpecsConstants.INTERACTION_SPECS[interaction.id]
          .needs_summary) {
      shortAnswerHtml = (
        this.explorationHtmlFormatterService.getShortAnswerHtml(
          this.data.learnerInput, interaction.id,
          interaction.customizationArgs));
    }
    return shortAnswerHtml;
  }

  getFeedbackAudioHighlightClass(): string {
    if (!this.isLastPair) {
      return '';
    }
    if (this.audioTranslationManagerService
      .getCurrentComponentName() ===
      AppConstants.COMPONENT_NAME_FEEDBACK &&
      (this.audioPlayerService.isPlaying() ||
      this.autogeneratedAudioPlayerService.isPlaying())) {
      return ExplorationPlayerConstants.AUDIO_HIGHLIGHT_CSS_CLASS;
    }
  }

  togglePopover(): void {
    this.popover.toggle();
  }
}

angular.module('oppia').directive('oppiaInputResponsePair',
  downgradeComponent({
    component: InputResponsePairComponent
  }) as angular.IDirectiveFactory);
