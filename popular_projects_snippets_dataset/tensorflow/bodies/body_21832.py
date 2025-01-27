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
    # TODO(b/70206927): Use ResourceVariables once they are handled properly.
    v_res = variables.VariableV1(1, name="v_res")
    w_res = variables.VariableV1(
        v_res,
        trainable=False,
        collections=[ops.GraphKeys.LOCAL_VARIABLES],
        name="w_res")
    x_res = variables.VariableV1(
        3 * v_res,
        trainable=False,
        collections=[ops.GraphKeys.LOCAL_VARIABLES],
        name="x_res")

    with self.cached_session():
        self.assertEqual(False, variables.is_variable_initialized(v).eval())
        self.assertEqual(False, variables.is_variable_initialized(w).eval())
        self.assertEqual(False, variables.is_variable_initialized(x).eval())
        self.assertEqual(False, variables.is_variable_initialized(v_res).eval())
        self.assertEqual(False, variables.is_variable_initialized(w_res).eval())
        self.assertEqual(False, variables.is_variable_initialized(x_res).eval())
    sm2 = session_manager.SessionManager(local_init_op=[
        w.initializer, x.initializer, w_res.initializer, x_res.initializer
    ])
    sess = sm2.prepare_session("", init_op=None)
    self.assertEqual(
        False,
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
    self.assertEqual(1, sess.run(w))
    self.assertEqual(3, sess.run(x))
    self.assertEqual(
        False,
        variables.is_variable_initialized(
            sess.graph.get_tensor_by_name("v_res:0")).eval(session=sess))
    self.assertEqual(
        True,
        variables.is_variable_initialized(
            sess.graph.get_tensor_by_name("w_res:0")).eval(session=sess))
    self.assertEqual(
        True,
        variables.is_variable_initialized(
            sess.graph.get_tensor_by_name("x_res:0")).eval(session=sess))
    self.assertEqual(1, sess.run(w_res))
    self.assertEqual(3, sess.run(x_res))
