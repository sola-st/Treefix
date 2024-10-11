# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with self.cached_session() as sess:
    coord = coordinator.Coordinator()
    threads = [
        threading.Thread(
            target=busy_wait_for_coord_stop, args=(coord,)) for _ in range(3)
    ]
    for t in threads:
        coord.register_thread(t)
        t.start()
    coord_sess = monitored_session._CoordinatedSession(sess, coord)
    coord_sess.close()
    for t in threads:
        self.assertFalse(t.is_alive())
    self.assertTrue(coord.should_stop())
    self.assertTrue(coord_sess.should_stop())
