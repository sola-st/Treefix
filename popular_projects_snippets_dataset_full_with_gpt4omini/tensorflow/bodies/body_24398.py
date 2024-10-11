# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session() as sess:
    x = variables.VariableV1(10.0, name="x")
    y = variables.VariableV1(20.0, name="y")
    cond = control_flow_ops.cond(
        x > y, lambda: math_ops.add(x, 1), lambda: math_ops.add(y, 1))

    sess.run(variables.global_variables_initializer())

    cond_result, dump = self._debug_run_and_get_dump(sess, cond)
    self.assertEqual(21, cond_result)

    self.assertAllClose(
        [21.0], dump.get_tensors("cond/Merge", 0, "DebugIdentity"))
