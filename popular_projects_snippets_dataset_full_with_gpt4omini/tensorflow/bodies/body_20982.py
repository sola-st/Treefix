# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
self._started_the_side_thread_already = False
self._lock = threading.Lock()
self._stored_exception_event = threading.Event()
self._calls_before_stopping = calls_before_stopping
self._exception_to_raise = (exception_to_raise or errors_impl.AbortedError(
    None, None, 'Aborted at N'))
