# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session(config=no_rewrite_session_config()) as sess:
    v = variables.VariableV1(10.0, name="v")
    delta = variables.VariableV1(1.0, name="delta")
    inc_v = state_ops.assign_add(v, delta, name="inc_v")

    sess.run(variables.global_variables_initializer())
    _, dump = self._debug_run_and_get_dump(sess, inc_v)

    self.assertEqual(
        ["delta", "delta/read", "inc_v", "v"],
        dump.find_some_path("delta", "v", include_reversed_ref=True))
    self.assertIsNone(dump.find_some_path("delta", "v"))
