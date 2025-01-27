# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with self.cached_session() as sess:
    c = constant_op.constant(0)
    v = array_ops.identity(c)
    coord = coordinator.Coordinator()
    coord_sess = monitored_session._CoordinatedSession(sess, coord)
    self.assertEqual(42, coord_sess.run(v, feed_dict={c: 42}))
