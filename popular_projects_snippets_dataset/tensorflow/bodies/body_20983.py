# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
while True:
    with self._lock:
        if self._calls_before_stopping == 0:
            try:
                raise self._exception_to_raise
            except Exception as e:  # pylint: disable=broad-except
                coord.request_stop(e)
                self._stored_exception_event.set()
                break
