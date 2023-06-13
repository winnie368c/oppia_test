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
 * @fileoverview Module for the donate page.
 */

import { NgModule } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { DonatePageComponent } from './donate-page.component';
import { SharedComponentsModule } from 'components/shared-component.module';
import { DonatePageRootComponent } from './donate-page-root.component';
import { CommonModule } from '@angular/common';
import { DonatePageRoutingModule } from './donate-page-routing.module';

@NgModule({
  imports: [
    CommonModule,
    SharedComponentsModule,
    DonatePageRoutingModule,
    NgbModule
  ],
  declarations: [
    DonatePageComponent,
    DonatePageRootComponent,
  ],
  entryComponents: [
    DonatePageComponent,
    DonatePageRootComponent,
  ]
})
export class DonatePageModule {}
