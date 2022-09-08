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
 * @fileoverview Module for the exploration editor page.
 */

import { APP_INITIALIZER, NgModule, StaticProvider } from '@angular/core';
import { BrowserModule, HAMMER_GESTURE_CONFIG } from '@angular/platform-browser';
import { downgradeComponent } from '@angular/upgrade/static';
import { HttpClientModule } from '@angular/common/http';
import { HTTP_INTERCEPTORS } from '@angular/common/http';
import { RouterModule } from '@angular/router';
import { APP_BASE_HREF } from '@angular/common';

import { MatPaginatorModule } from '@angular/material/paginator';
import { SharedComponentsModule } from 'components/shared-component.module';
import { CkEditorCopyToolbarComponent } from 'components/ck-editor-helpers/ck-editor-copy-toolbar/ck-editor-copy-toolbar.component';
import { OppiaAngularRootComponent } from
  'components/oppia-angular-root.component';
import { platformFeatureInitFactory, PlatformFeatureService } from
  'services/platform-feature.service';
import { RequestInterceptor } from 'services/request-interceptor.service';
import { StateParamChangesEditorComponent } from './editor-tab/state-param-changes-editor/state-param-changes-editor.component';
import { DeleteStateSkillModalComponent } from './editor-tab/templates/modal-templates/delete-state-skill-modal.component';
import { ParamChangesEditorDirective } from './param-changes-editor/param-changes-editor.component';
import { SwitchContentLanguageRefreshRequiredModalComponent } from 'pages/exploration-player-page/switch-content-language-refresh-required-modal.component';
import { InteractionExtensionsModule } from 'interactions/interactions.module';
import { SaveVersionMismatchModalComponent } from './modal-templates/save-version-mismatch-modal.component';
import { SaveValidationFailModalComponent } from './modal-templates/save-validation-fail-modal.component';
import { ChangesInHumanReadableFormComponent } from './changes-in-human-readable-form/changes-in-human-readable-form.component';
import { LostChangesModalComponent } from './modal-templates/lost-changes-modal.component';
import { WelcomeModalComponent } from './modal-templates/welcome-modal.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { StateDiffModalComponent } from './modal-templates/state-diff-modal.component';
import { PostPublishModalComponent } from './modal-templates/post-publish-modal.component';
import { ExplorationPublishModalComponent } from 'pages/exploration-editor-page/modal-templates/exploration-publish-modal.component';
import { EditorReloadingModalComponent } from './modal-templates/editor-reloading-modal.component';
import { ConfirmDiscardChangesModalComponent } from './modal-templates/confirm-discard-changes-modal.component';
import { CreateFeedbackThreadModalComponent } from './feedback-tab/templates/create-feedback-thread-modal.component';
import { PreviewSummaryTileModalComponent } from './settings-tab/templates/preview-summary-tile-modal.component';
import { WelcomeTranslationModalComponent } from './translation-tab/modal-templates/welcome-translation-modal.component';
import { DeleteExplorationModalComponent } from './settings-tab/templates/delete-exploration-modal.component';
import { RemoveRoleConfirmationModalComponent } from './settings-tab/templates/remove-role-confirmation-modal.component';
import { ReassignRoleConfirmationModalComponent } from './settings-tab/templates/reassign-role-confirmation-modal.component';
import { ModeratorUnpublishExplorationModalComponent } from './settings-tab/templates/moderator-unpublish-exploration-modal.component';
import { TransferExplorationOwnershipModalComponent } from './settings-tab/templates/transfer-exploration-ownership-modal.component';
import { HelpModalComponent } from './modal-templates/help-modal.component';
import { DeleteAudioTranslationModalComponent } from './translation-tab/modal-templates/delete-audio-translation-modal.component';
import { TranslationTabBusyModalComponent } from './translation-tab/modal-templates/translation-tab-busy-modal.component';
import { ConfirmDeleteStateModalComponent } from './editor-tab/templates/modal-templates/confirm-delete-state-modal.component';
import { PreviewSetParametersModalComponent } from './preview-tab/templates/preview-set-parameters-modal.component';
import { CheckRevertExplorationModalComponent } from './history-tab/modal-templates/check-revert-exploration-modal.component';
import { RevertExplorationModalComponent } from './history-tab/modal-templates/revert-exploration-modal.component';
import { ExplorationMetadataDiffModalComponent } from './modal-templates/exploration-metadata-diff-modal.component';
import { SmartRouterModule } from 'hybrid-router-module-provider';
import { AppErrorHandlerProvider } from 'pages/oppia-root/app-error-handler';
import { ExplorationTitleEditorComponent } from './exploration-title-editor/exploration-title-editor.component';
import { ExplorationObjectiveEditorComponent } from './exploration-objective-editor/exploration-objective-editor.component';
import { ExplorationMetadataModalComponent } from 'pages/exploration-editor-page/modal-templates/exploration-metadata-modal.component';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { ExplorationSaveModalComponent } from './modal-templates/exploration-save-modal.component';
import { EditorNavbarBreadcrumbComponent } from './editor-navigation/editor-navbar-breadcrumb.component';
import { ExplorationGraphModalComponent } from './editor-tab/templates/modal-templates/exploration-graph-modal.component';
import { ExplorationGraphComponent } from './editor-tab/graph-directives/exploration-graph.component';
import { StateNameEditorComponent } from './editor-tab/state-name-editor/state-name-editor.component';
import { EditorNavigationComponent } from './editor-navigation/editor-navigation.component';
import { TeachOppiaModalComponent } from './editor-tab/templates/modal-templates/teach-oppia-modal.component';
import { SettingsTabComponent } from './settings-tab/settings-tab.component';
import { UnresolvedAnswersOverviewComponent } from './editor-tab/unresolved-answers-overview/unresolved-answers-overview.component';
import { PreviewTabComponent } from './preview-tab/preview-tab.component';
import { HistoryTabComponent } from './history-tab/history-tab.component';

@NgModule({
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    InteractionExtensionsModule,
    // TODO(#13443): Remove smart router module provider once all pages are
    // migrated to angular router.
    SmartRouterModule,
    MatAutocompleteModule,
    ReactiveFormsModule,
    FormsModule,
    MatPaginatorModule,
    RouterModule.forRoot([]),
    SharedComponentsModule,
    ToastrModule.forRoot(toastrConfig)
  ],
  declarations: [
    CkEditorCopyToolbarComponent,
    DeleteStateSkillModalComponent,
    ParamChangesEditorDirective,
    StateParamChangesEditorComponent,
    SwitchContentLanguageRefreshRequiredModalComponent,
    SaveVersionMismatchModalComponent,
    SaveValidationFailModalComponent,
    ChangesInHumanReadableFormComponent,
    LostChangesModalComponent,
    WelcomeModalComponent,
    StateDiffModalComponent,
    PostPublishModalComponent,
    ConfirmDiscardChangesModalComponent,
    ExplorationPublishModalComponent,
    EditorReloadingModalComponent,
    CreateFeedbackThreadModalComponent,
    PreviewSummaryTileModalComponent,
    DeleteExplorationModalComponent,
    RemoveRoleConfirmationModalComponent,
    ReassignRoleConfirmationModalComponent,
    ModeratorUnpublishExplorationModalComponent,
    TransferExplorationOwnershipModalComponent,
    HelpModalComponent,
    ConfirmDeleteStateModalComponent,
    PreviewSetParametersModalComponent,
    CheckRevertExplorationModalComponent,
    RevertExplorationModalComponent,
    WelcomeTranslationModalComponent,
    DeleteAudioTranslationModalComponent,
    TranslationTabBusyModalComponent,
    ExplorationMetadataDiffModalComponent,
    ExplorationTitleEditorComponent,
    ExplorationObjectiveEditorComponent,
    ExplorationMetadataModalComponent,
    ExplorationSaveModalComponent,
    EditorNavbarBreadcrumbComponent,
    ExplorationGraphModalComponent,
    ExplorationGraphComponent,
    StateNameEditorComponent,
    EditorNavigationComponent,
    TeachOppiaModalComponent,
    SettingsTabComponent,
    UnresolvedAnswersOverviewComponent,
    PreviewTabComponent,
    HistoryTabComponent
  ],
  entryComponents: [
    CkEditorCopyToolbarComponent,
    DeleteStateSkillModalComponent,
    StateParamChangesEditorComponent,
    SwitchContentLanguageRefreshRequiredModalComponent,
    SaveVersionMismatchModalComponent,
    SaveValidationFailModalComponent,
    ChangesInHumanReadableFormComponent,
    LostChangesModalComponent,
    WelcomeModalComponent,
    StateDiffModalComponent,
    PostPublishModalComponent,
    ConfirmDiscardChangesModalComponent,
    ExplorationPublishModalComponent,
    EditorReloadingModalComponent,
    CreateFeedbackThreadModalComponent,
    PreviewSummaryTileModalComponent,
    DeleteExplorationModalComponent,
    RemoveRoleConfirmationModalComponent,
    ReassignRoleConfirmationModalComponent,
    ModeratorUnpublishExplorationModalComponent,
    TransferExplorationOwnershipModalComponent,
    HelpModalComponent,
    ConfirmDeleteStateModalComponent,
    PreviewSetParametersModalComponent,
    CheckRevertExplorationModalComponent,
    RevertExplorationModalComponent,
    WelcomeTranslationModalComponent,
    DeleteAudioTranslationModalComponent,
    TranslationTabBusyModalComponent,
    ExplorationMetadataDiffModalComponent,
    ExplorationTitleEditorComponent,
    ExplorationObjectiveEditorComponent,
    ExplorationMetadataModalComponent,
    ExplorationSaveModalComponent,
    EditorNavbarBreadcrumbComponent,
    ExplorationGraphModalComponent,
    ExplorationGraphComponent,
    StateNameEditorComponent,
    EditorNavigationComponent,
    TeachOppiaModalComponent,
    SettingsTabComponent,
    UnresolvedAnswersOverviewComponent,
    PreviewTabComponent,
    HistoryTabComponent
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
    },
    AppErrorHandlerProvider,
    {
      provide: APP_BASE_HREF,
      useValue: '/'
    }
  ]
})
class ExplorationEditorPageModule {
  // Empty placeholder method to satisfy the `Compiler`.
  ngDoBootstrap() {}
}

import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { downgradeModule } from '@angular/upgrade/static';
import { ToastrModule } from 'ngx-toastr';
import { MyHammerConfig, toastrConfig } from 'pages/oppia-root/app.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

const bootstrapFnAsync = async(extraProviders: StaticProvider[]) => {
  const platformRef = platformBrowserDynamic(extraProviders);
  return platformRef.bootstrapModule(ExplorationEditorPageModule);
};
const downgradedModule = downgradeModule(bootstrapFnAsync);

declare var angular: ng.IAngularStatic;

angular.module('oppia').requires.push(downgradedModule);

angular.module('oppia').directive(
  // This directive is the downgraded version of the Angular component to
  // bootstrap the Angular 8.
  'oppiaAngularRoot',
  downgradeComponent({
    component: OppiaAngularRootComponent
  }) as angular.IDirectiveFactory);
