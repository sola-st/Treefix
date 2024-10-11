# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with self.cached_session() as sess:
    coord = coordinator.Coordinator()
    coord_sess = monitored_session._CoordinatedSession(sess, coord)
    self.assertFalse(coord_sess.should_stop())
    coord_sess.close()
    self.assertTrue(coord_sess.should_stop())
