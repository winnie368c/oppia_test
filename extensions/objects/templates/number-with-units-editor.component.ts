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
 * @fileoverview Component for number with units editor.
 */

import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { downgradeComponent } from '@angular/upgrade/static';
import { ObjectFormValidityChangeEvent } from 'app-events/app-events';
import { EventBusGroup, EventBusService } from 'app-events/event-bus.service';
import { NumberWithUnitsObjectFactory } from 'domain/objects/NumberWithUnitsObjectFactory';
import { NumberWithUnitsAnswer } from 'interactions/answer-defs';

@Component({
  selector: 'number-with-units-editor',
  templateUrl: './number-with-units-editor.component.html',
  styleUrls: []
})
export class NumberWithUnitsEditorComponent implements OnInit {
  // These properties are initialized using Angular lifecycle hooks
  // and we need to do non-null assertion, for more information see
  // https://github.com/oppia/oppia/wiki/Guide-on-defining-types#ts-7-1
  @Input() modalId!: symbol;
  // 'value' will be null if user has not input any value.
  @Input() value!: NumberWithUnitsAnswer | null;
  @Output() valueChanged = new EventEmitter();
  numberWithUnitsString!: string;
  errorMessage: string = '';
  eventBusGroup: EventBusGroup;

  constructor(
    private eventBusService: EventBusService,
    private numberWithUnitsObjectFactory: NumberWithUnitsObjectFactory) {
    this.eventBusGroup = new EventBusGroup(this.eventBusService);
  }

  ngOnInit(): void {
    if (this.value !== null) {
      const defaultNumberWithUnits =
        this.numberWithUnitsObjectFactory.fromDict(this.value);
      this.numberWithUnitsString = defaultNumberWithUnits.toString();
      this.valueChanged.emit(this.value);
    }
  }

  updateValue(newValue: string): void {
    try {
      let numberWithUnits =
        this.numberWithUnitsObjectFactory.fromRawInputString(newValue);
      this.value = numberWithUnits;
      this.valueChanged.emit(this.value);
      this.eventBusGroup.emit(new ObjectFormValidityChangeEvent({
        value: false,
        modalId: this.modalId
      }));
    } catch (parsingError: unknown) {
      this.eventBusGroup.emit(new ObjectFormValidityChangeEvent({
        value: true,
        modalId: this.modalId
      }));
      if (parsingError instanceof Error) {
        this.errorMessage = parsingError.message;
      }
    }
  }
}

angular.module('oppia').directive('numberWithUnitsEditor', downgradeComponent({
  component: NumberWithUnitsEditorComponent
}) as angular.IDirectiveFactory);
