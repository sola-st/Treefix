# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager_test.py
with ops.Graph().as_default():
    v = variables.VariableV1(1, name="v")
    w = variables.VariableV1(
        v,
        trainable=False,
        collections=[ops.GraphKeys.LOCAL_VARIABLES],
        name="w")
    x = variables.VariableV1(
        3 * v,
        trainable=False,
        collections=[ops.GraphKeys.LOCAL_VARIABLES],
        name="x")
    with self.cached_session():
        self.assertEqual(False, variables.is_variable_initialized(v).eval())
        self.assertEqual(False, variables.is_variable_initialized(w).eval())
        self.assertEqual(False, variables.is_variable_initialized(x).eval())
    sm2 = session_manager.SessionManager(
        ready_op=variables.report_uninitialized_variables(),
        ready_for_local_init_op=variables.report_uninitialized_variables(
            variables.global_variables()),
        local_init_op=[w.initializer, x.initializer])
    sess = sm2.prepare_session("", init_op=v.initializer)
    self.assertEqual(
        True,
        variables.is_variable_initialized(
            sess.graph.get_tensor_by_name("v:0")).eval(session=sess))
    self.assertEqual(
        True,
        variables.is_variable_initialized(
            sess.graph.get_tensor_by_name("w:0")).eval(session=sess))
    self.assertEqual(
        True,
        variables.is_variable_initialized(
            sess.graph.get_tensor_by_name("x:0")).eval(session=sess))
    self.assertEqual(1, sess.run(v))
    self.assertEqual(1, sess.run(w))
    self.assertEqual(3, sess.run(x))
