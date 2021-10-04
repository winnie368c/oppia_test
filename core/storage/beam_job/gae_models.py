# coding: utf-8
#
# Copyright 2021 The Oppia Authors. All Rights Reserved.
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

"""Models for managing Apache Beam jobs."""

from __future__ import absolute_import
from __future__ import unicode_literals

import enum
import uuid

from core import utils
from core.platform import models

(base_models,) = models.Registry.import_models([models.NAMES.base_model])

datastore_services = models.Registry.import_datastore_services()

_MAX_ID_GENERATION_ATTEMPTS = 5


def _get_new_model_id(model_class: base_models.BaseModel) -> str:
    """Generates an ID for a new model.

    Returns:
        str. The new ID.
    """
    for _ in range(_MAX_ID_GENERATION_ATTEMPTS):
        new_id = utils.convert_to_hash(uuid.uuid4().hex, 22)
        if model_class.get(new_id, strict=False) is None:
            return new_id
    raise RuntimeError('Failed to generate a unique ID after %d attempts' % (
        _MAX_ID_GENERATION_ATTEMPTS))


class BeamJobState(enum.Enum):
    """Constants from an enum defined by Google Cloud Dataflow, which are thus
    outside of our control:
    https://cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#jobstate
    """

    # The job is currently running.
    RUNNING = 'RUNNING'
    # The job has been created but is not yet running. Jobs that are pending may
    # only transition to RUNNING, or FAILED.
    PENDING = 'PENDING'
    # The job has not yet started to run.
    STOPPED = 'STOPPED'
    # The job has has been explicitly cancelled and is in the process of
    # stopping. Jobs that are cancelling may only transition to CANCELLED or
    # FAILED.
    CANCELLING = 'CANCELLING'
    # The job has has been explicitly cancelled. This is a terminal job state.
    # This state may only be set via a Cloud Dataflow jobs.update call, and only
    # if the job has not yet reached another terminal state.
    CANCELLED = 'CANCELLED'
    # The job is in the process of draining. A draining job has stopped pulling
    # from its input sources and is processing any data that remains in-flight.
    # This state may be set via a Cloud Dataflow jobs.update call, but only as a
    # transition from RUNNING. Jobs that are draining may only transition to
    # DRAINED, CANCELLED, or FAILED.
    DRAINING = 'DRAINING'
    # The job has been drained. A drained job terminated by stopping pulling
    # from its input sources and processing any data that remained in-flight
    # when draining was requested. This state is a terminal state, may only be
    # set by the Cloud Dataflow service, and only as a transition from DRAINING.
    DRAINED = 'DRAINED'
    # The job was successfully updated, meaning that this job was stopped and
    # another job was started, inheriting state from this one. This is a
    # terminal job state. This state may only be set by the Cloud Dataflow
    # service, and only as a transition from RUNNING.
    UPDATED = 'UPDATED'
    # The job has successfully completed. This is a terminal job state. This
    # state may be set by the Cloud Dataflow service, as a transition from
    # RUNNING. It may also be set via a Cloud Dataflow jobs.update call, if the
    # job has not yet reached a terminal state.
    DONE = 'DONE'
    # The job has has failed. This is a terminal job state. This state may only
    # be set by the Cloud Dataflow service, and only as a transition from
    # RUNNING.
    FAILED = 'FAILED'
    # The job's run state isn't specified.
    UNKNOWN = 'UNKNOWN'


class BeamJobRunModel(base_models.BaseModel):
    """Represents the execution of an individual Apache Beam job.

    The IDs of BeamJobRunResultModel are used by BeamJobRunResultModel, and
    generated by using the urlsafe base64 encoding of a uuid() value:
    ^[A-Za-z0-9-_]{22}$.
    """

    # The ID of the dataflow job this model corresponds to. If the job is run
    # synchronously, then this value will be empty.
    # https://cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#resource:-job
    dataflow_job_id = (
        datastore_services.StringProperty(required=False, indexed=True))
    # The name of the job class that implements the job's logic.
    job_name = datastore_services.StringProperty(required=True, indexed=True)
    # The state of the job at the time the model was last updated.
    latest_job_state = datastore_services.StringProperty(
        required=True, indexed=True, choices=[
            BeamJobState.RUNNING.value,
            BeamJobState.PENDING.value,
            BeamJobState.STOPPED.value,
            BeamJobState.CANCELLING.value,
            BeamJobState.CANCELLED.value,
            BeamJobState.DRAINING.value,
            BeamJobState.DRAINED.value,
            BeamJobState.UPDATED.value,
            BeamJobState.DONE.value,
            BeamJobState.FAILED.value,
            BeamJobState.UNKNOWN.value,
        ])

    @classmethod
    def get_new_id(cls) -> str:
        """Generates an ID for a new BeamJobRunModel.

        Returns:
            str. The new ID.
        """
        return _get_new_model_id(cls)

    @staticmethod
    def get_deletion_policy():
        """Model doesn't contain any data directly corresponding to a user."""
        return base_models.DELETION_POLICY.NOT_APPLICABLE

    @staticmethod
    def get_model_association_to_user():
        """Model doesn't contain user data."""
        return base_models.MODEL_ASSOCIATION_TO_USER.NOT_CORRESPONDING_TO_USER

    @classmethod
    def get_export_policy(cls):
        """Model doesn't contain any data directly corresponding to a user."""
        return dict(super(BeamJobRunModel, cls).get_export_policy(), **{
            'dataflow_job_id': base_models.EXPORT_POLICY.NOT_APPLICABLE,
            'job_name': base_models.EXPORT_POLICY.NOT_APPLICABLE,
            'latest_job_state': base_models.EXPORT_POLICY.NOT_APPLICABLE,
        })


class BeamJobRunResultModel(base_models.BaseModel):
    """Represents the result of an Apache Beam job.

    IMPORTANT: Datastore entities have a size limit of ~1MiB (1,048,572 bytes,
    to be precise). To support jobs that may need to produce outputs that exceed
    this this limit, BeamJobRunResultModels are split into _unordered_ batches.
    Thus, to return the full results you must fetch all models with matching
    job_model_id values and concatenate their results.

    The IDs of BeamJobRunResultModel are inconsequential, and generated by using
    the urlsafe base64 encoding of a uuid() value: ^[A-Za-z0-9-_]{22}$.
    """

    # The ID of the BeamJobRunResultModel corresponding to the result.
    job_id = datastore_services.StringProperty(required=True, indexed=True)
    # The standard text output generated by the corresponding Apache Beam job.
    stdout = datastore_services.TextProperty(required=False, indexed=False)
    # The error output generated by the corresponding Apache Beam job.
    stderr = datastore_services.TextProperty(required=False, indexed=False)

    @classmethod
    def get_new_id(cls) -> str:
        """Generates an ID for a new BeamJobRunResultModel.

        Returns:
            str. The new ID.
        """
        return _get_new_model_id(cls)

    @staticmethod
    def get_deletion_policy():
        """Model doesn't contain any data directly corresponding to a user."""
        return base_models.DELETION_POLICY.NOT_APPLICABLE

    @staticmethod
    def get_model_association_to_user():
        """Model doesn't contain user data."""
        return base_models.MODEL_ASSOCIATION_TO_USER.NOT_CORRESPONDING_TO_USER

    @classmethod
    def get_export_policy(cls):
        """Model doesn't contain any data directly corresponding to a user."""
        return dict(super(BeamJobRunResultModel, cls).get_export_policy(), **{
            'job_id': base_models.EXPORT_POLICY.NOT_APPLICABLE,
            'stdout': base_models.EXPORT_POLICY.NOT_APPLICABLE,
            'stderr': base_models.EXPORT_POLICY.NOT_APPLICABLE,
        })
