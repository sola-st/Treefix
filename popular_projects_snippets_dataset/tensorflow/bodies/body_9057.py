# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Run the given resource closure with preemption handling."""
assert closure.tag == self.worker_index
try:
    with self.failure_handler.wait_on_failure(
        on_failure_fn=self._on_resource_closure_failure,
        on_transient_failure_fn=(
            lambda: self._process_resource_closure(closure)),
        on_recovery_fn=self._on_worker_recovery,
        worker_device_name=self.device_name):
        closure.execute_on(self)
except Exception as e:  # pylint: disable=broad-except
    # Avoid logging the derived cancellation error
    logging.info("[Worker %d] got an exception when processing resource "
                 "closure", self.worker_index)
    if not isinstance(e, errors.CancelledError):
        logging.error(
            " /job:worker/task:%d encountered the following error when "
            "processing resource closure: %r:%s", self.worker_index, e, e)
    closure.maybe_call_with_output_remote_value(lambda r: r._set_error(e))  # pylint: disable=protected-access
