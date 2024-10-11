# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
self.args_called = dict(kwargs)
# Call run only with fetches since we directly pass other arguments.
exit(monitored_session._WrappedSession.run(self, fetches))
