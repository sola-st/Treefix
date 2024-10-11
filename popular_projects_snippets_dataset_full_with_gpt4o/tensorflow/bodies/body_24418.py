# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session() as sess:
    a = variables.VariableV1(
        [42], dtype=np.float32, name="numeric_summary_uninit/a")

    _, dump = self._debug_run_and_get_dump(
        sess, a.initializer, debug_ops=["DebugNumericSummary"])

    self.assertTrue(dump.loaded_partition_graphs())

    # DebugNumericSummary output should reflect the uninitialized state of
    # the watched tensor.
    numeric_summary = dump.get_tensors("numeric_summary_uninit/a", 0,
                                       "DebugNumericSummary")[0]
    self.assertAllClose([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                        numeric_summary[0:8])
    # Check dtype (index 12), ndims (index 13) and dimension sizes (index
    # 14+).
    self.assertAllClose([1.0, 1.0, 1.0], numeric_summary[12:])
    self.assertTrue(np.isinf(numeric_summary[8]))
    self.assertGreater(numeric_summary[8], 0.0)
    self.assertTrue(np.isinf(numeric_summary[9]))
    self.assertLess(numeric_summary[9], 0.0)
    self.assertTrue(np.isnan(numeric_summary[10]))
    self.assertTrue(np.isnan(numeric_summary[11]))
