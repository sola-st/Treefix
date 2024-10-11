# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with self.cached_session() as sess:
    constant_op.constant(0.0)
    coord = coordinator.Coordinator()
    coord_sess = monitored_session._CoordinatedSession(sess, coord)
    self.assertEqual(sess.graph, coord_sess.graph)
    self.assertEqual(sess.sess_str, coord_sess.sess_str)
