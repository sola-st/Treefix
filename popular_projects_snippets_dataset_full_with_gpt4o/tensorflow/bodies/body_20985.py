# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
stopping_now = False
with self._lock:
    self._calls_before_stopping -= 1
    if self._calls_before_stopping == 0:
        stopping_now = True

if stopping_now:
    self._stored_exception_event.wait()
