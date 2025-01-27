# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with self.cached_session() as sess:
    constant_op.constant(0.0)
    wrapped_sess = monitored_session._WrappedSession(sess)
    self.assertEqual(sess.graph, wrapped_sess.graph)
    self.assertEqual(sess.sess_str, wrapped_sess.sess_str)
