# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session.py
self._coord.request_stop()
try:
    self._coord.join(
        stop_grace_period_secs=self._stop_grace_period_secs,
        ignore_live_threads=True)
finally:
    try:
        _WrappedSession.close(self)
    except Exception:  # pylint: disable=broad-except
        # We intentionally suppress exceptions from the close() here since
        # useful exceptions are already reported by join().
        pass
