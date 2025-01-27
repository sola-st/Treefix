# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with self.cached_session() as sess:
    c = constant_op.constant(0)
    v = array_ops.identity(c)
    coord = coordinator.Coordinator()
    threads = [
        threading.Thread(
            target=busy_wait_for_coord_stop, args=(coord,)) for _ in range(3)
    ]
    for t in threads:
        coord.register_thread(t)
        t.start()
    coord_sess = monitored_session._CoordinatedSession(sess, coord)
    self.assertFalse(coord_sess.should_stop())
    for t in threads:
        self.assertTrue(t.is_alive())
    self.assertEqual(0, coord_sess.run(c))
    for t in threads:
        self.assertTrue(t.is_alive())
    self.assertEqual(1, coord_sess.run(v, feed_dict={c: 1}))
    for t in threads:
        self.assertTrue(t.is_alive())
    with self.assertRaisesRegex(TypeError, 'None has invalid type'):
        coord_sess.run([None], feed_dict={c: 2})
    coord_sess.close()
    for t in threads:
        self.assertFalse(t.is_alive())
    self.assertTrue(coord.should_stop())
    self.assertTrue(coord_sess.should_stop())
