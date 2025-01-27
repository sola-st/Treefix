# Extracted from ./data/repos/tensorflow/tensorflow/python/training/session_manager_test.py
# Regression test. Previously Variable._build_initializer_expr would enter
# into an infinite recursion when the variable's initial_value involved
# cyclic dependencies.
with ops.Graph().as_default():
    i = control_flow_ops.while_loop(lambda i: i < 1, lambda i: i + 1, [0])
    v = variables.VariableV1(array_ops.identity(i), name="v")
    with self.cached_session():
        self.assertEqual(False, variables.is_variable_initialized(v).eval())
    sm = session_manager.SessionManager(
        ready_op=variables.report_uninitialized_variables())
    sess = sm.prepare_session("", init_op=v.initializer)
    self.assertEqual(1, sess.run(v))
    self.assertEqual(
        True,
        variables.is_variable_initialized(
            sess.graph.get_tensor_by_name("v:0")).eval(session=sess))
