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
 * @fileoverview Component for the side navigation bar.
 */

import { ChangeDetectorRef, Component, Input } from '@angular/core';
import { downgradeComponent } from '@angular/upgrade/static';
import { AppConstants } from 'app.constants';
import { ClassroomBackendApiService } from 'domain/classroom/classroom-backend-api.service';
import { UrlInterpolationService } from 'domain/utilities/url-interpolation.service';
import { SiteAnalyticsService } from 'services/site-analytics.service';
import { UserService } from 'services/user.service';
import { WindowRef } from 'services/contextual/window-ref.service';
import { CreatorTopicSummary } from 'domain/topic/creator-topic-summary.model';
import { SidebarStatusService } from 'services/sidebar-status.service';
import { AccessValidationBackendApiService } from 'pages/oppia-root/routing/access-validation-backend-api.service';

 @Component({
   selector: 'oppia-side-navigation-bar',
   templateUrl: './side-navigation-bar.component.html'
 })
export class SideNavigationBarComponent {
  // These properties are initialized using Angular lifecycle hooks
  // and we need to do non-null assertion, for more information see
  // https://github.com/oppia/oppia/wiki/Guide-on-defining-types#ts-7-1
   @Input() display!: boolean;

   currentUrl!: string;
   classroomData: CreatorTopicSummary[] = [];
   topicSummariesLength: number = 0;
   CLASSROOM_PROMOS_ARE_ENABLED: boolean = false;
   getinvolvedSubmenuIsShown: boolean = false;
   learnSubmenuIsShown: boolean = true;
   userIsLoggedIn!: boolean;

   PAGES_REGISTERED_WITH_FRONTEND = (
     AppConstants.PAGES_REGISTERED_WITH_FRONTEND);

   constructor(
     private classroomBackendApiService: ClassroomBackendApiService,
     private accessValidationBackendApiService:
      AccessValidationBackendApiService,
     private changeDetectorRef: ChangeDetectorRef,
     private siteAnalyticsService: SiteAnalyticsService,
     private userService: UserService,
     private sidebarStatusService: SidebarStatusService,
     private urlInterpolationService: UrlInterpolationService,
     private windowRef: WindowRef
   ) {}

   getStaticImageUrl(imagePath: string): string {
     return this.urlInterpolationService.getStaticImageUrl(imagePath);
   }

   ngOnInit(): void {
     this.currentUrl = this.windowRef.nativeWindow.location.pathname;

     let service = this.classroomBackendApiService;
     service.fetchClassroomPromosAreEnabledStatusAsync().then(
       classroomPromosAreEnabled => {
         this.CLASSROOM_PROMOS_ARE_ENABLED = classroomPromosAreEnabled;
       });

     this.userService.getUserInfoAsync().then((userInfo) => {
       this.userIsLoggedIn = userInfo.isLoggedIn();
     });
   }

   ngAfterViewChecked(): void {
     if (this.CLASSROOM_PROMOS_ARE_ENABLED) {
       this.accessValidationBackendApiService.validateAccessToClassroomPage(
         'math').then(()=>{
         this.classroomBackendApiService.fetchClassroomDataAsync(
           'math').then((classroomData) => {
           this.classroomData = classroomData.getTopicSummaries();
         });
       });
     }

     this.changeDetectorRef.detectChanges();
   }

   stopclickfurther(event: Event): void {
     event.stopPropagation();
   }

   closeSidebarOnSwipeleft(): void {
     this.sidebarStatusService.closeSidebar();
   }

   togglelearnSubmenu(): void {
     this.learnSubmenuIsShown = !this.learnSubmenuIsShown;
   }

   togglegetinvolvedSubmenu(): void {
     this.getinvolvedSubmenuIsShown =
     !this.getinvolvedSubmenuIsShown;
     this.learnSubmenuIsShown = false;
   }

   navigateToClassroomPage(classroomUrl: string): void {
     this.siteAnalyticsService.registerClassroomHeaderClickEvent();
     setTimeout(() => {
       this.windowRef.nativeWindow.location.href = classroomUrl;
     }, 150);
   }
}

angular.module('oppia').directive('oppiaSideNavigationBar',
   downgradeComponent({
     component: SideNavigationBarComponent
   }) as angular.IDirectiveFactory);
