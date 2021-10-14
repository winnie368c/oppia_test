// Copyright 2016 The Oppia Authors. All Rights Reserved.
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
 * @fileoverview Component for the error page.
 */

import { Component, Input, OnInit } from '@angular/core';
import { downgradeComponent } from '@angular/upgrade/static';

import { UrlInterpolationService } from
  'domain/utilities/url-interpolation.service';
import { PageTitleService } from 'services/page-title.service';

@Component({
  selector: 'error-page',
  templateUrl: './error-page.component.html',
  styleUrls: []
})
export class ErrorPageComponent implements OnInit {
  @Input() statusCode: string;
  constructor(
    private urlInterpolationService: UrlInterpolationService,
    private pageTitleService: PageTitleService) {}

  ngOnInit(): void {
    this.pageTitleService.setDocumentTitle(
      'Error ' + this.statusCode + ' - Oppia');
  }

  getStaticImageUrl(imagePath: string): string {
    return this.urlInterpolationService.getStaticImageUrl(imagePath);
  }

  getStatusCode(): number {
    return Number(this.statusCode);
  }
}

angular.module('oppia').directive(
  'errorPage', downgradeComponent(
    {component: ErrorPageComponent}));
