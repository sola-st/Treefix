# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py

wrapper = TestDebugWrapperSession(self._sess, self._dump_root,
                                  self._observer)

# No matrix size mismatch.
self.assertAllClose(
    np.array([[11.0], [-1.0]]),
    wrapper.run(self._q, feed_dict={self._ph: np.array([[1.0], [2.0]])}))
self.assertEqual(1, self._observer["on_run_end_count"])
self.assertIsNone(self._observer["tf_error"])

# Now there should be a matrix size mismatch error.
wrapper.run(self._q, feed_dict={self._ph: np.array([[1.0], [2.0], [3.0]])})
self.assertEqual(2, self._observer["on_run_end_count"])
self.assertTrue(
    isinstance(self._observer["tf_error"], errors.InvalidArgumentError))
