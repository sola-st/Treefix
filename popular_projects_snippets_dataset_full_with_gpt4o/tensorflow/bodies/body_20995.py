# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with self.cached_session() as sess:
    c = constant_op.constant(0)
    v = array_ops.identity(c)
    recoverable_sess = monitored_session._RecoverableSession(
        self._SessionReturner(sess))
    self.assertEqual(51, recoverable_sess.run(v, feed_dict={c: 51}))
