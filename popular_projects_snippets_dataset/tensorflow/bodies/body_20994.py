# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with self.cached_session() as sess:
    constant_op.constant(0.0)
    recoverable_sess = monitored_session._RecoverableSession(
        self._SessionReturner(sess))
    self.assertEqual(sess.graph, recoverable_sess.graph)
    self.assertEqual(sess.sess_str, recoverable_sess.sess_str)
