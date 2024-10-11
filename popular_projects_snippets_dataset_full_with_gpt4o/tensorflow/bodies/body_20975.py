# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with self.cached_session() as sess:
    c = constant_op.constant(0)
    v = array_ops.identity(c)
    coord = coordinator.Coordinator()
    coord_sess = monitored_session._CoordinatedSession(sess, coord)
    self.assertFalse(coord_sess.should_stop())
    self.assertEqual(0, coord_sess.run(c))
    self.assertEqual(1, coord_sess.run(v, feed_dict={c: 1}))
    with self.assertRaisesRegex(TypeError, 'None has invalid type'):
        coord_sess.run([None], feed_dict={c: 2})
    self.assertFalse(coord.should_stop())
    self.assertFalse(coord_sess.should_stop())
