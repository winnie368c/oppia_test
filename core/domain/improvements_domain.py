# coding: utf-8
#
# Copyright 2020 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Domain objects related to Oppia improvement tasks."""

from __future__ import annotations

import datetime

from core import feconf
from core import utils
from core.constants import constants

from typing import Optional, TypedDict


class TaskEntryDict(TypedDict):
    """Dict for TaskEntry object."""

    entity_type: str
    entity_id: str
    entity_version: int
    task_type: str
    target_type: str
    target_id: str
    issue_description: Optional[str]
    status: str
    resolver_username: Optional[str]
    resolved_on_msecs: Optional[float]


class TaskEntry:
    """Domain object representing an actionable task from the improvements tab.

    Attributes:
        entity_type: str. The type of entity the task entry refers to.
            For example, "exploration".
        entity_id: str. The ID of the entity the task entry refers to.
            For example, an exploration ID.
        entity_version: int. The version of the entity the task entry refers to.
            For example, an exploration's version.
        task_type: str. The type of task the task entry tracks.
        target_type: str. The type of sub-entity the task entry refers to.
            For example, "state" when entity type is "exploration".
        target_id: str. The ID of the sub-entity the task entry refers to.
            For example, the state name of an exploration.
        issue_description: str or None. The sentence generated by Oppia to
            describe why the task was created.
        status: str. Tracks the state/progress of the task entry.
        resolver_id: str or None. The corresponding user who resolved this task.
        resolved_on: datetime or None. The datetime at which this task was
            resolved.
    """

    def __init__(
        self,
        entity_type: str,
        entity_id: str,
        entity_version: int,
        task_type: str,
        target_type: str,
        target_id: str,
        issue_description: Optional[str],
        status: str,
        resolver_id: Optional[str] = None,
        resolved_on: Optional[datetime.datetime] = None
    ) -> None:
        """Initializes a new TaskEntry domain object from the given values.

        Args:
            entity_type: str. The type of entity the task entry refers to.
                For example: "exploration".
            entity_id: str. The ID of the entity the task entry refers to.
                For example: an exploration ID.
            entity_version: int. The version of the entity the task entry refers
                to. For example: an exploration's version.
            task_type: str. The type of task the task entry tracks.
            target_type: str. The type of sub-entity the task entry refers to.
                For example, when entity type is "exploration": "state".
            target_id: str. The ID of the sub-entity the task entry refers to.
                For example, the state name of an exploration.
            issue_description: str. The sentence generated by Oppia to describe
                why the task was created.
            status: str. Tracks the state/progress of the task entry.
            resolver_id: str. The corresponding user who resolved this task.
                Only used when status is resolved, otherwise replaced with None.
            resolved_on: datetime. The datetime at which this task was resolved.
                Only used when status is resolved, otherwise replaced with None.
        """
        if status != constants.TASK_STATUS_RESOLVED:
            resolver_id = None
            resolved_on = None
        self.entity_type = entity_type
        self.entity_id = entity_id
        self.entity_version = entity_version
        self.task_type = task_type
        self.target_type = target_type
        self.target_id = target_id
        self.issue_description = issue_description
        self.status = status
        self.resolver_id = resolver_id
        self.resolved_on = resolved_on

    @property
    def task_id(self) -> str:
        """Returns the unique identifier of this task.

        Value has the form: "[entity_type].[entity_id].[entity_version].
                             [task_type].[target_type].[target_id]"

        Returns:
            str. The ID of this task.
        """
        return feconf.TASK_ENTRY_ID_TEMPLATE % (
            self.entity_type, self.entity_id, self.entity_version,
            self.task_type, self.target_type, self.target_id)

    @property
    def composite_entity_id(self) -> str:
        """Utility field which results in a 20% speedup compared to querying by
        each of the invididual fields used to compose it.

        Value has the form: "[entity_type].[entity_id].[entity_version]".

        Returns:
            str. The value of the utility field.
        """
        return feconf.COMPOSITE_ENTITY_ID_TEMPLATE % (
            self.entity_type, self.entity_id, self.entity_version)

    def to_dict(self) -> TaskEntryDict:
        """Returns a dict-representation of the task.

        Returns:
            dict. Contains the following keys:
                entity_type: str. The type of entity the task entry refers to.
                    For example, "exploration".
                entity_id: str. The ID of the entity the task entry refers to.
                    For example, an exploration ID.
                entity_version: int. The version of the entity the task entry
                    refers to. For example, an exploration's version.
                task_type: str. The type of task the task entry tracks.
                target_type: str. The type of sub-entity the task entry refers
                    to. For example, "state" when entity type is "exploration".
                target_id: str. The ID of the sub-entity the task entry refers
                    to. For example, the state name of an exploration.
                issue_description: str. The sentence generated by Oppia to
                    describe why the task was created.
                status: str. Tracks the state/progress of the task entry.
                resolver_username: str|None. Username of the user who resolved
                    the task when status is resolved. Otherwise None.
                resolved_on_msecs: float|None. Time in
                    milliseconds since epoch at which the task was resolved
                    when status is resolved. Otherwise None.
        """

        return {
            'entity_type': self.entity_type,
            'entity_id': self.entity_id,
            'entity_version': self.entity_version,
            'task_type': self.task_type,
            'target_type': self.target_type,
            'target_id': self.target_id,
            'issue_description': self.issue_description,
            'status': self.status,
            'resolver_username': None,
            'resolved_on_msecs': (
                None if not self.resolved_on
                else utils.get_time_in_millisecs(self.resolved_on)),
        }
