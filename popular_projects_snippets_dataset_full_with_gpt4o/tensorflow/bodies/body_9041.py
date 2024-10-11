# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Sets error and unblocks any wait() call."""
with self._queue_lock:
    # TODO(yuefengz): maybe record all failure and give users more
    # information?
    if self._inflight_closure_count < 1:
        raise AssertionError("There is no inflight closures to mark_failed.")
    if self._error is None:
        self._error = e
    self._inflight_closure_count -= 1
    if self._inflight_closure_count == 0:
        self._no_inflight_closure_condition.notify_all()
    self._stop_waiting_condition.notify_all()
