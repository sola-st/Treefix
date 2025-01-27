# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Runs a closure with preemption handling."""
try:
    with self.failure_handler.wait_on_failure(
        on_failure_fn=lambda e: self._on_closure_failure(closure, e),
        on_transient_failure_fn=(
            lambda: self._cluster.closure_queue.put_back(closure)),
        on_recovery_fn=self._on_worker_recovery,
        worker_device_name=self.device_name):
        closure.execute_on(self)
        with metric_utils.monitored_timer("remote_value_fetch"):
            # Copy the remote tensor to local (the coordinator) in case worker
            # becomes unavailable at a later time.
            closure.maybe_call_with_output_remote_value(lambda r: r.get())
        self._cluster.closure_queue.mark_finished()
except Exception as e:  # pylint: disable=broad-except
    # Avoid logging the derived cancellation error
    if not isinstance(e, errors.CancelledError):
        logging.error(
            " /job:worker/task:%d encountered the following error when "
            "processing closure: %r:%s", self.worker_index, e, e)
    closure.maybe_call_with_output_remote_value(lambda r: r._set_error(e))  # pylint: disable=protected-access
    self._cluster.closure_queue.mark_failed(e)
