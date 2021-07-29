// Copyright 2020 The Oppia Authors. All Rights Reserved.
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
 * @fileoverview About-page-root component.
 */

import { Component } from '@angular/core';
import { AppConstants } from 'app.constants';
import { MetaAttribute, MetaTagCustomizationService } from 'services/contextual/meta-tag-customization.service';
import { PageTitleService } from 'services/page-title.service';

@Component({
  selector: 'oppia-about-page-root',
  templateUrl: './about-page-root.component.html'
})
export class AboutPageRootComponent {
  constructor(
    private pageTitleService: PageTitleService,
    private metaTagCustomizationService: MetaTagCustomizationService
  ) {}

  ngOnInit(): void {
    let pageData = AppConstants.PAGES_REGISTERED_WITH_FRONTEND.ABOUT;
    // Update default title.
    this.pageTitleService.setPageTitle(pageData.TITLE);

    let metaAttributes: MetaAttribute[] = [];
    for (let i = 0; i < pageData.META.length; i++) {
      metaAttributes.push({
        propertyType: pageData.META[i].PROPERTY_TYPE,
        propertyValue: pageData.META[i].PROPERTY_VALUE,
        content: pageData.META[i].CONTENT
      });
    }
    // Update meta tags.
    this.metaTagCustomizationService.addOrReplaceMetaTags(metaAttributes);
  }
}
