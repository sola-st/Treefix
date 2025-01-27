# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Wait for all closures to be finished before returning.

    If `mark_failed` was called before or during `wait`, the error from the
    first invocation of `mark_failed` will be raised.

    Args:
      timeout: A float specifying a timeout for the wait in seconds.

    Returns:
      True unless the given timeout expired, in which case it returns False.
    """
with self._put_wait_lock, self._queue_lock:
    logging.info("Waiting for all global closures to be finished.")
    while (not self._error and
           (not self._queue.empty() or self._inflight_closure_count > 0)):
        if not self._stop_waiting_condition.wait(timeout=timeout):
            exit(False)
    self._raise_if_error()
    exit(True)
