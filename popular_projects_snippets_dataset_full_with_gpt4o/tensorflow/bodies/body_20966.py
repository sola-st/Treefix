# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with self.cached_session() as sess:
    wrapped_sess = StopAtNSession(sess, 3)
    self.assertFalse(wrapped_sess.should_stop())
    self.assertFalse(wrapped_sess.should_stop())
    self.assertFalse(wrapped_sess.should_stop())
    self.assertTrue(wrapped_sess.should_stop())
