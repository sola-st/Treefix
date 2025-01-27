# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
self._initial_session = session
# We only have one session per test case. We can't re-create it, thus
# it shouldn't be closed.
self._initial_session.close = lambda *args: None
self._create_session_calls = 0
