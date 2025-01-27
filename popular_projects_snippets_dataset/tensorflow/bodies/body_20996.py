# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
self.sessions_to_use = [
    AbortAtNSession(sess, x + 1) for x in range(3)
]
