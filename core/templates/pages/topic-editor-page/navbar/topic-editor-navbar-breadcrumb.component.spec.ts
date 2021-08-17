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
 * @fileoverview Unit tests for the navbar breadcrumb of the topic editor.
 */

import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { Subtopic } from 'domain/topic/subtopic.model';
import { TopicObjectFactory } from 'domain/topic/TopicObjectFactory';
import { TopicEditorRoutingService } from '../services/topic-editor-routing.service';
import { TopicEditorStateService } from '../services/topic-editor-state.service';
import { TopicEditorNavbarBreadcrumbComponent } from './topic-editor-navbar-breadcrumb.component';
import { HttpClientTestingModule } from '@angular/common/http/testing';

describe('TopicEditorNavbarBreadcrumbComponent', () => {
  let component: TopicEditorNavbarBreadcrumbComponent;
  let fixture: ComponentFixture<TopicEditorNavbarBreadcrumbComponent>;
  let topicEditorStateService: TopicEditorStateService;
  let topicObjectFactory: TopicObjectFactory;
  let topicEditorRoutingService: TopicEditorRoutingService;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      declarations: [TopicEditorNavbarBreadcrumbComponent]
    }).compileComponents();
  }));

  beforeEach(() => {
    topicEditorRoutingService = TestBed.get(TopicEditorRoutingService);
    topicEditorStateService = TestBed.inject(TopicEditorStateService);
    topicObjectFactory = TestBed.inject(TopicObjectFactory);
    fixture = TestBed.createComponent(TopicEditorNavbarBreadcrumbComponent);
    component = fixture.componentInstance;
  });

  it('should initialise component when user opens topic editor page', () => {
    let topic = topicObjectFactory.createInterstitialTopic();
    let subtopic1 = Subtopic.createFromTitle(1, 'Subtopic1');
    subtopic1.setUrlFragment('subtopic-one');
    let subtopic2 = Subtopic.createFromTitle(1, 'Subtopic2');
    subtopic2.setUrlFragment('subtopic-two');
    let subtopic3 = Subtopic.createFromTitle(1, 'Subtopic3');
    subtopic3.setUrlFragment('subtopic-three');
    topic.getSubtopics = () => {
      return [subtopic1, subtopic2, subtopic3];
    };
    spyOn(topicEditorStateService, 'getTopic').and.returnValue(topic);

    component.ngOnInit();

    expect(component.topic).toEqual(topic);
  });

  it('should navigate to main tab when user clicks \'Back to Topic\'', () => {
    spyOn(topicEditorRoutingService, 'navigateToMainTab');

    component.navigateToMainTab();

    expect(topicEditorRoutingService.navigateToMainTab).toHaveBeenCalled();
  });

  it('should return true when the current tab is in a subtopic', () => {
    spyOn(topicEditorRoutingService, 'getActiveTabName').and.returnValue(
      'subtopic_editor');
    spyOn(topicEditorRoutingService, 'getLastTabVisited').and.returnValue(
      'topic_preview');

    expect(component.canNavigateToTopicEditorPage()).toBeTrue();
  });

  it('should return true when the last visited tab is subtopic', () => {
    spyOn(topicEditorRoutingService, 'getActiveTabName').and.returnValue(
      'topic_editor');
    spyOn(topicEditorRoutingService, 'getLastTabVisited').and.returnValue(
      'subtopic');

    expect(component.canNavigateToTopicEditorPage()).toBeTrue();
  });

  it('should return false when user cannot navigate to topic editor ' +
  'page', () => {
    spyOn(topicEditorRoutingService, 'getActiveTabName').and.returnValue(
      'topic_preview');
    spyOn(topicEditorRoutingService, 'getLastTabVisited').and.returnValue(
      'main');

    expect(component.canNavigateToTopicEditorPage()).toBeFalse();
  });
});
