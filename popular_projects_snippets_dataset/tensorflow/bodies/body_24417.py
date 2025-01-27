# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session(config=no_rewrite_session_config()) as sess:
    a = variables.VariableV1(
        [
            np.nan, np.nan, 0.0, 0.0, 0.0, -1.0, -3.0, 3.0, 7.0, -np.inf,
            -np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.nan, np.nan
        ],
        dtype=np.float32,
        name="numeric_summary/a")
    b = variables.VariableV1(
        [0.0] * 18, dtype=np.float32, name="numeric_summary/b")
    c = math_ops.add(a, b, name="numeric_summary/c")

    sess.run(variables.global_variables_initializer())

    _, dump = self._debug_run_and_get_dump(
        sess, c, debug_ops=["DebugNumericSummary"])
    self.assertTrue(dump.loaded_partition_graphs())

    self.assertAllClose([[
        1.0, 18.0, 4.0, 2.0, 2.0, 3.0, 2.0, 5.0, -3.0, 7.0, 0.85714286,
        8.97959184, 1.0, 1.0, 18.0
    ]], dump.get_tensors("numeric_summary/a/read", 0, "DebugNumericSummary"))
