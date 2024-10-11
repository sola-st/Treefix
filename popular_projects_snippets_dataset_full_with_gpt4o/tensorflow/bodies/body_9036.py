# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Put a closure into the queue for later execution.

    If `mark_failed` was called before `put`, the error from the first
    invocation of `mark_failed` will be raised.

    Args:
      closure: The `Closure` to put into the queue.
      tag: if not None, put into a queue with the given tag.
    """
closure.tag = tag
if tag is not None:
    with self._queue_lock:
        self._tagged_queue[tag].put(closure, block=False)
        self._closures_queued_condition.notifyAll()
else:
    with self._put_wait_lock, self._queue_lock:
        self._queue_free_slot_condition.wait_for(lambda: not self._queue.full())
        self._queue.put(closure, block=False)
        self._raise_if_error()
        self._closures_queued_condition.notify()
