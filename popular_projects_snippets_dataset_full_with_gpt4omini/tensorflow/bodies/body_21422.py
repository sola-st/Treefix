# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator.py
"""Wait for threads to terminate.

    This call blocks until a set of threads have terminated.  The set of thread
    is the union of the threads passed in the `threads` argument and the list
    of threads that registered with the coordinator by calling
    `Coordinator.register_thread()`.

    After the threads stop, if an `exc_info` was passed to `request_stop`, that
    exception is re-raised.

    Grace period handling: When `request_stop()` is called, threads are given
    'stop_grace_period_secs' seconds to terminate.  If any of them is still
    alive after that period expires, a `RuntimeError` is raised.  Note that if
    an `exc_info` was passed to `request_stop()` then it is raised instead of
    that `RuntimeError`.

    Args:
      threads: List of `threading.Threads`. The started threads to join in
        addition to the registered threads.
      stop_grace_period_secs: Number of seconds given to threads to stop after
        `request_stop()` has been called.
      ignore_live_threads: If `False`, raises an error if any of the threads are
        still alive after `stop_grace_period_secs`.

    Raises:
      RuntimeError: If any thread is still alive after `request_stop()`
        is called and the grace period expires.
    """
# Threads registered after this call will not be joined.
with self._lock:
    if threads is None:
        threads = self._registered_threads
    else:
        threads = self._registered_threads.union(set(threads))
    # Copy the set into a list to avoid race conditions where a new thread
    # is added while we are waiting.
    threads = list(threads)

# Wait for all threads to stop or for request_stop() to be called.
while any(t.is_alive() for t in threads) and not self.wait_for_stop(1.0):
    pass

# If any thread is still alive, wait for the grace period to expire.
# By the time this check is executed, threads may still be shutting down,
# so we add a sleep of increasing duration to give them a chance to shut
# down without losing too many cycles.
# The sleep duration is limited to the remaining grace duration.
stop_wait_secs = 0.001
while any(t.is_alive() for t in threads) and stop_grace_period_secs >= 0.0:
    time.sleep(stop_wait_secs)
    stop_grace_period_secs -= stop_wait_secs
    stop_wait_secs = 2 * stop_wait_secs
    # Keep the waiting period within sane bounds.
    # The minimum value is to avoid decreasing stop_wait_secs to a value
    # that could cause stop_grace_period_secs to remain unchanged.
    stop_wait_secs = max(min(stop_wait_secs, stop_grace_period_secs), 0.001)

# List the threads still alive after the grace period.
stragglers = [t.name for t in threads if t.is_alive()]

# Terminate with an exception if appropriate.
with self._lock:
    self._joined = True
    self._registered_threads = set()
    if self._exc_info_to_raise:
        _, ex_instance, _ = self._exc_info_to_raise
        raise ex_instance
    elif stragglers:
        if ignore_live_threads:
            logging.info("Coordinator stopped with threads still running: %s",
                         " ".join(stragglers))
        else:
            raise RuntimeError(
                "Coordinator stopped with threads still running: %s" %
                " ".join(stragglers))
