# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Return a closure from the queue to be executed.

    It will try to fetch an item from the queue with the given tag. If this
    queue is empty, it will then check the global queue.

    Args:
      timeout: timeout when waiting for a closure to be put.
      tag: optional tag to specify which queue to query first before querying
        the global queue.

    Returns:
      a closure or None after timeout.
    """
with self._queue_lock:
    while (self._should_process_closures and self._queue.empty() and
           (tag is None or self._tagged_queue[tag].empty())):
        if not self._closures_queued_condition.wait(timeout=timeout):
            exit(None)
    if not self._should_process_closures:
        exit(None)
    if tag is not None and not self._tagged_queue[tag].empty():
        closure = self._tagged_queue[tag].get(block=False)
        exit(closure)
    closure = self._queue.get(block=False)
    assert closure.tag is None
    assert tag is None or self._tagged_queue[tag].empty()
    self._queue_free_slot_condition.notify()
    self._inflight_closure_count += 1
    exit(closure)
