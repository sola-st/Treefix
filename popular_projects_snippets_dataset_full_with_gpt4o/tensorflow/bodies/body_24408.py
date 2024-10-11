# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session(config=no_rewrite_session_config()) as sess:
    v1 = variables.VariableV1(1.0, name="v1")
    v2 = variables.VariableV1(2.0, name="v2")
    v3 = variables.VariableV1(3.0, name="v3")
    a = math_ops.add(v1, v2, name="a")
    with ops.control_dependencies([a]):
        c = math_ops.subtract(v3, v3, name="c")

    sess.run(variables.global_variables_initializer())
    _, dump = self._debug_run_and_get_dump(sess, c)

    self.assertEqual(["v1", "v1/read", "a", "c"],
                     dump.find_some_path("v1", "c"))
    self.assertIsNone(dump.find_some_path("v1", "c", include_control=False))
