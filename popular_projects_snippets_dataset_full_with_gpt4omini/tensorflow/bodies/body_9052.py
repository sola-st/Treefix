# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Set the resource ABORTED and add an error to it."""
# TODO(yuefengz): maybe we can query whether a tensor is valid or not
# instead of marking a tensor aborted?
logging.info("[Worker %d] Clearing all resources.", self.worker_index)
for weakref_resource in self._resource_remote_value_refs:
    resource = weakref_resource()
    if resource:
        # It is important to set an error on an aborted RemoteValue from a
        # ResourceClosure because its failure will not trigger the worker thread
        # to raise error immediately and the worker may continue executing
        # closures taking it as an input. The error will then be correctly
        # reported to users.
        resource._set_aborted(ClosureAbortedError(e))  # pylint: disable=protected-access
