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
 * @fileoverview Module for the pending account deletion page.
 */

import { APP_INITIALIZER, NgModule } from '@angular/core';
import { BrowserModule, HAMMER_GESTURE_CONFIG } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { HTTP_INTERCEPTORS } from '@angular/common/http';
import { RequestInterceptor } from 'services/request-interceptor.service';
import { SharedComponentsModule } from 'components/shared-component.module';
import { platformFeatureInitFactory, PlatformFeatureService } from
  'services/platform-feature.service';
import { PendingAccountDeletionPageComponent } from './pending-account-deletion-page.component';
import { SharedPipesModule } from 'filters/shared-pipes.module';
import { TranslateModule } from '@ngx-translate/core';
import { PendingAccountDeletionPageRootComponent } from './pending-account-deletion-page-root.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MyHammerConfig } from 'pages/oppia-root/app.module';

@NgModule({
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    SharedComponentsModule,
    SharedPipesModule,
    TranslateModule
  ],
  declarations: [
    PendingAccountDeletionPageComponent,
    PendingAccountDeletionPageRootComponent,
  ],
  entryComponents: [
    PendingAccountDeletionPageComponent,
    PendingAccountDeletionPageRootComponent,
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: RequestInterceptor,
      multi: true
    },
    {
      provide: APP_INITIALIZER,
      useFactory: platformFeatureInitFactory,
      deps: [PlatformFeatureService],
      multi: true
    },
    {
      provide: HAMMER_GESTURE_CONFIG,
      useClass: MyHammerConfig
    }
  ],
  bootstrap: [PendingAccountDeletionPageRootComponent]
})
export class PendingAccountDeletionPageModule {}
