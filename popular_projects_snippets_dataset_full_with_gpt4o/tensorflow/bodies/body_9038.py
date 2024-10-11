# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Let the queue know that a closure has been successfully executed."""
with self._queue_lock:
    if self._inflight_closure_count < 1:
        raise AssertionError("There is no inflight closures to mark_finished.")
    self._inflight_closure_count -= 1
    if self._inflight_closure_count == 0:
        self._no_inflight_closure_condition.notify_all()
    if self._queue.empty() and self._inflight_closure_count == 0:
        self._stop_waiting_condition.notify_all()
    self._watchdog.report_closure_done()
