# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with self.cached_session() as sess:
    c = constant_op.constant(0)
    v = array_ops.identity(c)
    self.assertEqual(42, sess.run(v, feed_dict={c: 42}))
    wrapped_sess = monitored_session._WrappedSession(sess)
    self.assertEqual(51, wrapped_sess.run(v, feed_dict={c: 51}))
