# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
_, _ = scaffold, session
if not self.init_raised_aborted_error:
    self.init_raised_aborted_error = True
    raise errors_impl.AbortedError(None, None, 'Abort')
