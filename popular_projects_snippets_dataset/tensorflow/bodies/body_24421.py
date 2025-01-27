# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session(config=no_rewrite_session_config()) as sess:
    a = variables.VariableV1(10.0, name="a")
    b = variables.VariableV1(0.0, name="b")
    c = variables.VariableV1(0.0, name="c")

    x = math_ops.divide(a, b, name="x")
    y = math_ops.multiply(x, c, name="y")

    sess.run(variables.global_variables_initializer())

    # Here, validate=False is necessary to avoid causality check error.
    # TODO(cais): Maybe let DebugDumpDir constructor automatically ignore
    #   debug ops with mute_if_healthy=false attribute during validation.
    _, dump = self._debug_run_and_get_dump(
        sess, y, debug_ops=["DebugNumericSummary(mute_if_healthy=true)"],
        validate=False)

    self.assertLessEqual(2, dump.size)
    self.assertAllClose([[
        1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, np.inf, -np.inf, np.nan,
        np.nan, 1.0, 0.0
    ]], dump.get_tensors("x", 0, "DebugNumericSummary"))
    self.assertAllClose([[
        1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, np.inf, -np.inf, np.nan,
        np.nan, 1.0, 0.0
    ]], dump.get_tensors("y", 0, "DebugNumericSummary"))

    # Another run with the default mute_if_healthy (false) value should
    # dump all the tensors.
    file_io.delete_recursively(self._dump_root)
    _, dump = self._debug_run_and_get_dump(
        sess, y, debug_ops=["DebugNumericSummary()"])
    self.assertLessEqual(8, dump.size)
