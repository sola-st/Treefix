# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
wrapper = TestDebugWrapperSession(self._sess, self._dump_root,
                                  self._observer)

with wrapper as sess:
    self.assertAllClose([[3.0], [4.0]], self._s)
    self.assertEqual(1, self._observer["on_run_start_count"])
    self.assertEqual(self._s, self._observer["run_fetches"])
    self.assertEqual(1, self._observer["on_run_end_count"])

    self.assertAllClose(
        [[11.0], [-1.0]],
        sess.run(self._q, feed_dict={self._ph: np.array([[1.0], [2.0]])}))
    self.assertEqual(2, self._observer["on_run_start_count"])
    self.assertEqual(self._q, self._observer["run_fetches"])
    self.assertEqual(2, self._observer["on_run_end_count"])
