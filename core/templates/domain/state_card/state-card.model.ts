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
 * @fileoverview Model class for creating new frontend instances of State
 * card domain objects used in the exploration player.
 */

import cloneDeep from 'lodash/cloneDeep';

import { AppConstants } from 'app.constants';
import { AudioTranslationLanguageService } from
  'pages/exploration-player-page/services/audio-translation-language.service';
import { Interaction } from 'domain/exploration/InteractionObjectFactory';
import { BindableVoiceovers, RecordedVoiceovers } from
  'domain/exploration/recorded-voiceovers.model';
import { InteractionCustomizationArgs } from
  'interactions/customization-args-defs';
import { Hint } from 'domain/exploration/HintObjectFactory';
import { Solution } from 'domain/exploration/SolutionObjectFactory';

import { WrittenTranslations } from
  'domain/exploration/WrittenTranslationsObjectFactory';
import { InteractionSpecsConstants, InteractionSpecsKey } from 'pages/interaction-specs.constants';

export interface InputResponsePair {
  learnerInput: string,
  // 'oppiaResponse' is null when the response for the input has
  // not been received yet.
  oppiaResponse: string | null,
  isHint: boolean
}

export class StateCard {
  _stateName: string;
  _contentHtml: string;
  _interactionHtml: string;
  _interaction: Interaction;
  _inputResponsePairs: InputResponsePair[];
  _recordedVoiceovers: RecordedVoiceovers;
  _writtenTranslations: WrittenTranslations;
  _contentId: string;
  _completed: boolean;
  audioTranslationLanguageService: AudioTranslationLanguageService;
  constructor(
      stateName: string, contentHtml: string,
      interactionHtml: string, interaction: Interaction,
      inputResponsePairs: InputResponsePair[],
      recordedVoiceovers: RecordedVoiceovers,
      writtenTranslations: WrittenTranslations,
      contentId: string,
      audioTranslationLanguageService: AudioTranslationLanguageService) {
    this._stateName = stateName;
    this._contentHtml = contentHtml;
    this._interactionHtml = interactionHtml;
    this._inputResponsePairs = inputResponsePairs;
    this._interaction = interaction;
    this._recordedVoiceovers = recordedVoiceovers;
    this._writtenTranslations = writtenTranslations;
    this._contentId = contentId;
    this._completed = false;
    this.audioTranslationLanguageService = audioTranslationLanguageService;
  }

  // Restore everything immutably so that Angular can detect changes.
  restoreImmutable(stateCard: StateCard): void {
    Object.assign(this, stateCard);
  }

  getStateName(): string {
    return this._stateName;
  }

  getInteraction(): Interaction {
    return this._interaction;
  }

  getVoiceovers(): BindableVoiceovers {
    let recordedVoiceovers = this._recordedVoiceovers;
    let contentId = this._contentId;
    if (recordedVoiceovers) {
      return recordedVoiceovers.getBindableVoiceovers(contentId);
    }
    return {};
  }

  getRecordedVoiceovers(): RecordedVoiceovers {
    return this._recordedVoiceovers;
  }

  isContentAudioTranslationAvailable(): boolean {
    return Object.keys(
      this.getVoiceovers()).length > 0 ||
        this.audioTranslationLanguageService.isAutogeneratedAudioAllowed();
  }

  getInteractionId(): string | null {
    if (this.getInteraction()) {
      return this.getInteraction().id;
    }
    return null;
  }

  isTerminal(): boolean {
    let interactionId = this.getInteractionId();
    return (
      Boolean(interactionId) &&
      InteractionSpecsConstants.INTERACTION_SPECS[
        <InteractionSpecsKey>interactionId].is_terminal);
  }

  getHints(): Hint[] {
    return this.getInteraction().hints;
  }

  // A null 'solution' indicates that this Interaction does not have a hint
  // or there is a hint, but no solution.
  getSolution(): Solution | null {
    return this.getInteraction().solution;
  }

  doesInteractionSupportHints(): boolean {
    let interactionId = this.getInteractionId();
    if (interactionId) {
      return (
        !InteractionSpecsConstants.INTERACTION_SPECS[
          <InteractionSpecsKey>interactionId].is_terminal &&
        !InteractionSpecsConstants.INTERACTION_SPECS[
          <InteractionSpecsKey>interactionId].is_linear
      );
    }
    return false;
  }

  isCompleted(): boolean {
    return this._completed;
  }

  markAsCompleted(): void {
    this._completed = true;
  }

  markAsNotCompleted(): void {
    this._completed = false;
  }

  // Some interaction specifications do not have instructions, thus we return
  // 'null' in that case.
  getInteractionInstructions(): string | null {
    let interactionId = this.getInteractionId();
    if (interactionId) {
      return (
        InteractionSpecsConstants.INTERACTION_SPECS[
          <InteractionSpecsKey>interactionId].instructions
      );
    }
    return null;
  }

  // This returns 'null' when no interaction is set for the card.
  getInteractionCustomizationArgs(): InteractionCustomizationArgs | null {
    let interaction = this.getInteraction();
    if (!interaction) {
      return null;
    }
    return interaction.customizationArgs;
  }

  isInteractionInline(): boolean {
    let interactionId = this.getInteractionId();
    if (interactionId) {
      var interactionDisplayMode: string | null = (
        InteractionSpecsConstants.INTERACTION_SPECS[
          <InteractionSpecsKey>interactionId].display_mode);
    } else {
      var interactionDisplayMode: string | null = null;
    }
    return (
      !interactionId ||
      interactionDisplayMode === AppConstants.INTERACTION_DISPLAY_MODE_INLINE);
  }

  getContentHtml(): string {
    return this._contentHtml;
  }

  getInteractionHtml(): string {
    return this._interactionHtml;
  }

  // This will return null when the response for the input has
  // not been received yet.
  getOppiaResponse(index: number): string | null {
    return this._inputResponsePairs[index].oppiaResponse;
  }

  getInputResponsePairs(): InputResponsePair[] {
    return this._inputResponsePairs;
  }

  // This will return null if there are no input response pairs present.
  getLastInputResponsePair(): InputResponsePair | null {
    if (this._inputResponsePairs.length === 0) {
      return null;
    }
    return this._inputResponsePairs[this._inputResponsePairs.length - 1];
  }

  // This will return null when there is no input response pair.
  getLastAnswer(): string | null {
    const lastInputResponsePair = this.getLastInputResponsePair();
    if (lastInputResponsePair === null) {
      return null;
    }
    return lastInputResponsePair.learnerInput;
  }


  // This will return null when no previous response exists.
  getLastOppiaResponse(): string | null {
    const lastInputResponsePair = this.getLastInputResponsePair();
    if (lastInputResponsePair === null) {
      return null;
    }
    return lastInputResponsePair.oppiaResponse;
  }

  addInputResponsePair(inputResponsePair: InputResponsePair): void {
    this._inputResponsePairs.push(cloneDeep(inputResponsePair));
  }

  setLastOppiaResponse(response: string): void {
    // This check is added here to ensure that this._inputReponsePairs is
    // accessed only if there is atleast one input response pair present.
    // In the editor preview tab if a user clicks on restart from beginning
    // option just after submitting an answer for a card while the response
    // is still loading, this function is called after
    // this._inputResponsePairs is set to null as we are starting from the
    // first card again. Adding a check here makes sure that element at index
    // -1 is not accessed even in the above case.
    if (this._inputResponsePairs.length >= 1) {
      this._inputResponsePairs[
        this._inputResponsePairs.length - 1].oppiaResponse = response;
    }
  }

  setInteractionHtml(interactionHtml: string): void {
    this._interactionHtml = interactionHtml;
  }

  get writtenTranslations(): WrittenTranslations {
    return cloneDeep(this._writtenTranslations);
  }

  get contentHtml(): string {
    return this._contentHtml;
  }

  set contentHtml(html: string) {
    this._contentHtml = html;
  }

  get contentId(): string {
    return this._contentId;
  }

  /**
   * @param {string} stateName - The state name for the current card.
   * @param {string} contentHtml - The HTML string for the content displayed
   *        on the content card.
   * @param {string} interactionHtml - The HTML that calls the interaction
   *        directive for the current card.
   * @param {Interaction} interaction - An interaction object that stores all
   *        the properties of the card's interaction.
   * @param {RecordedVoiceovers} recordedVoiceovers
   * @param {string} contentId
   * @param {AudioTranslationLanguageService} audioTranslationLanguageService
   */
  static createNewCard(
      stateName: string, contentHtml: string, interactionHtml: string,
      interaction: Interaction, recordedVoiceovers: RecordedVoiceovers,
      writtenTranslations: WrittenTranslations, contentId: string,
      audioTranslationLanguageService: AudioTranslationLanguageService
  ): StateCard {
    return new StateCard(
      stateName, contentHtml, interactionHtml,
      cloneDeep(interaction), [],
      recordedVoiceovers, writtenTranslations, contentId,
      audioTranslationLanguageService);
  }
}
