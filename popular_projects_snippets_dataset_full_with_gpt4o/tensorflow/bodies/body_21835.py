# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager_test.py
with ops.Graph().as_default():
    v = variables.VariableV1(1, name="v")
    w = variables.VariableV1(
        v,
        trainable=False,
        collections=[ops.GraphKeys.LOCAL_VARIABLES],
        name="w")
    with self.cached_session():
        self.assertEqual(False, variables.is_variable_initialized(v).eval())
        self.assertEqual(False, variables.is_variable_initialized(w).eval())
    sm2 = session_manager.SessionManager(
        ready_op=variables.report_uninitialized_variables())
    with self.assertRaisesRegex(RuntimeError,
                                "Init operations did not make model ready"):
        sm2.prepare_session("", init_op=[v.initializer])
