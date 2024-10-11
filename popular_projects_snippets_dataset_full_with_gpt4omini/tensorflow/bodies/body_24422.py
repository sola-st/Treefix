# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session() as sess:
    a = variables.VariableV1([10.0, 10.0], name="a")
    b = variables.VariableV1([10.0, 2.0], name="b")

    x = math_ops.add(a, b, name="x")  # [20.0, 12.0]
    y = math_ops.divide(x, b, name="y")  # [2.0, 6.0]

    sess.run(variables.global_variables_initializer())

    # Here, validate=False is necessary to avoid causality check error.
    # TODO(cais): Maybe let DebugDumpDir constructor automatically ignore
    #   debug ops with mute_if_healthy=false attribute during validation.
    _, dump = self._debug_run_and_get_dump(
        sess, y, debug_ops=[
            "DebugNumericSummary(mute_if_healthy=true; upper_bound=11.0)"],
        validate=False)

    self.assertEqual(1, dump.size)
    self.assertAllClose([[
        1.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 12.0, 20.0, 16.0, 16.0, 1.0,
        1.0, 2.0]], dump.get_tensors("x", 0, "DebugNumericSummary"))
