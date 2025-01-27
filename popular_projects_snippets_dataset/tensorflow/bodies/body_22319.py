# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
# Mock out logging calls so we can verify whether correct tensors are being
# monitored.
self._actual_log = tf_logging.info
self.logged_message = None

def mock_log(*args, **kwargs):
    self.logged_message = args
    self._actual_log(*args, **kwargs)

tf_logging.info = mock_log
