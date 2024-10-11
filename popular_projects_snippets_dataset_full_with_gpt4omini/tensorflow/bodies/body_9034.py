# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Clears the queue and sets remaining closures cancelled error.

    This method expects self._queue_lock to be held prior to entry.
    """
self._cancellation_mgr.start_cancel()
logging.info("Canceling all closures: waiting for inflight closures to "
             "finish")
while self._inflight_closure_count > 0:
    self._no_inflight_closure_condition.wait()
logging.info("Canceling all closures: canceling remaining closures on the "
             "queue")
while True:
    try:
        closure = self._queue.get(block=False)
        self._queue_free_slot_condition.notify()
        closure.mark_cancelled()
    except queue.Empty:
        break
    # The cancellation manager cannot be reused once cancelled. After all
    # closures (queued or inflight) are cleaned up, recreate the cancellation
    # manager with clean state.
    # Note on thread-safety: this is triggered when one of theses
    # ClusterCoordinator APIs are called: `schedule`, `wait`, and `done`. At the
    # same time, no new closures can be constructed (which reads the
    # _cancellation_mgr to get cancellable functions).
self._cancellation_mgr = cancellation.CancellationManager()
