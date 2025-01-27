# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if self._cached_session is not None:
    self._cached_session.close()
    self._cached_session = None
