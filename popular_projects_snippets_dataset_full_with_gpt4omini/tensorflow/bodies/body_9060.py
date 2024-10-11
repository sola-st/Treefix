# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Synchronously creates a per-worker resource represented by a `RemoteValue`.

    Args:
      function: the resource function to be run remotely. It should be a
        `tf.function`, a concrete function or a Python function.
      args: positional arguments to be passed to the function.
      kwargs: keyword arguments to be passed to the function.

    Returns:
      one or several RemoteValue objects depending on the function return
      values.
    """
# Some notes about the concurrency: currently all the activities related to
# the same worker such as creating resources, setting resources' aborted
# status, and executing closures happen on the same thread. This allows us
# to have simpler logic of concurrency.

closure = ResourceClosure(
    function,
    self._cluster.resource_cancellation_mgr,
    args=args,
    kwargs=kwargs)
resource_remote_value = closure.build_output_remote_value()
with self._resource_tracking_lock:
    self._register_resource(resource_remote_value)
    if self._is_dead_with_error:
        resource_remote_value._set_aborted(  # pylint: disable=protected-access
            ClosureAbortedError(self._is_dead_with_error))
    else:
        self._schedule_resource(closure)
exit(resource_remote_value)
