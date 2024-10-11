# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
wrapper = TestDebugWrapperSession(
    self._sess, self._dump_root, self._observer)

# Check initial state of the observer.
self.assertEqual(0, self._observer["on_run_start_count"])
self.assertEqual(0, self._observer["on_run_end_count"])

s = wrapper.run(self._s)

# Assert the run return value is correct.
self.assertAllClose(np.array([[3.0], [4.0]]), s)

# Assert the on-run-start method is invoked.
self.assertEqual(1, self._observer["on_run_start_count"])

# Assert the on-run-start request reflects the correct fetch.
self.assertEqual(self._s, self._observer["run_fetches"])

# Assert the on-run-start request reflects the correct feed_dict.
self.assertIsNone(self._observer["run_feed_dict"])

# Assert the file debug URL has led to dump on the filesystem.
dump = debug_data.DebugDumpDir(self._dump_root)
self.assertEqual(7, len(dump.dumped_tensor_data))

# Assert the on-run-end method is invoked.
self.assertEqual(1, self._observer["on_run_end_count"])

# Assert the performed action field in the on-run-end callback request is
# correct.
self.assertEqual(
    framework.OnRunStartAction.DEBUG_RUN,
    self._observer["performed_action"])

# No TensorFlow runtime error should have happened.
self.assertIsNone(self._observer["tf_error"])
