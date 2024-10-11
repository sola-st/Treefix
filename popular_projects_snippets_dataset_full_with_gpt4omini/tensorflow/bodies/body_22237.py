# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Stop the services and the coordinator.

    This does not close the session.

    Args:
      threads: Optional list of threads to join with the coordinator.  If
        `None`, defaults to the threads running the standard services, the
        threads started for `QueueRunners`, and the threads started by the
        `loop()` method.  To wait on additional threads, pass the list in this
        parameter.
      close_summary_writer: Whether to close the `summary_writer`.  Defaults to
        `True` if the summary writer was created by the supervisor, `False`
        otherwise.
      ignore_live_threads: If `True` ignores threads that remain running after a
        grace period when joining threads via the coordinator, instead of
        raising a RuntimeError.
    """
self._coord.request_stop()
try:
    # coord.join() re-raises the first reported exception; the "finally"
    # block ensures that we clean up whether or not an exception was
    # reported.
    self._coord.join(
        threads,
        stop_grace_period_secs=self._stop_grace_secs,
        ignore_live_threads=ignore_live_threads)
finally:
    # Close the writer last, in case one of the running threads was using it.
    if close_summary_writer and self._summary_writer:
        # Stop messages are not logged with event.step,
        # since the session may have already terminated.
        self._summary_writer.add_session_log(SessionLog(status=SessionLog.STOP))
        self._summary_writer.close()
        self._graph_added_to_summary = False
