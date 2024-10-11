# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with self.cached_session() as sess:
    wrapped_sess0 = StopAtNSession(sess, 4)
    wrapped_sess1 = monitored_session._WrappedSession(wrapped_sess0)
    self.assertFalse(wrapped_sess1.should_stop())
    self.assertFalse(wrapped_sess1.should_stop())
    self.assertFalse(wrapped_sess1.should_stop())
    self.assertFalse(wrapped_sess1.should_stop())
    self.assertTrue(wrapped_sess1.should_stop())
