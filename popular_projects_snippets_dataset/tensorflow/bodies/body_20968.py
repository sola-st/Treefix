# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with self.cached_session() as sess:
    wrapped_sess = monitored_session._WrappedSession(sess)
    wrapped_sess.close()
    self.assertTrue(wrapped_sess.should_stop())
    wrapped_sess.close()
    self.assertTrue(wrapped_sess.should_stop())
