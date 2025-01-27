# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Executes the closure on the given worker.

    Args:
      worker: a `Worker` object.
    """
replica_args = _select_worker_slice(worker.worker_index, self._args)
replica_kwargs = _select_worker_slice(worker.worker_index, self._kwargs)

e = (
    _get_error_from_remote_values(replica_args) or
    _get_error_from_remote_values(replica_kwargs))
if e:
    if not isinstance(e, ClosureInputError):
        e = ClosureInputError(e)
    raise e

with ops.device(worker.device_name):
    with context.executor_scope(worker.executor):
        with coordinator_context.with_dispatch_context(worker):
            with metric_utils.monitored_timer("closure_execution"):
                output_values = self._function(
                    *nest.map_structure(_maybe_get_remote_value, replica_args),
                    **nest.map_structure(_maybe_get_remote_value, replica_kwargs))
self.maybe_call_with_output_remote_value(
    lambda r: r._set_values(output_values))  # pylint: disable=protected-access
