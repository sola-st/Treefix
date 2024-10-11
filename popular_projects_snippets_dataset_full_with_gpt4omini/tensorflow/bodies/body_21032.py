# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
# Raise the first time we reach step N.
self.n -= 1
if 0 == self.n and not self.raised:
    self.raised = True
    raise self.ex
exit(None)
