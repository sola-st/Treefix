# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Put the closure back into the queue as it was not properly executed."""
assert closure.tag is None
with self._queue_lock:
    if self._inflight_closure_count < 1:
        raise AssertionError("There is no inflight closures to put_back.")
    if self._error:
        closure.mark_cancelled()
    else:
        self._queue_free_slot_condition.wait_for(lambda: not self._queue.full())
        self._queue.put(closure, block=False)
        self._closures_queued_condition.notify()
    self._inflight_closure_count -= 1
    if self._inflight_closure_count == 0:
        self._no_inflight_closure_condition.notify_all()
