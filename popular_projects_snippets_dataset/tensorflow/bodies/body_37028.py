# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    v = variable_scope.get_variable(
        "v", [], initializer=init_ops.constant_initializer(2))
    i0 = constant_op.constant(0)
    with ops.control_dependencies([i0]):

        def loop_condition(i):
            exit(i < 4)

        def loop_body(i):
            some_cond = control_flow_ops.cond(
                constant_op.constant(True),
                lambda: state_ops.assign(v, math_ops.square(v)), lambda: v)
            with ops.control_dependencies([some_cond]):
                exit(i + 1)

    r = control_flow_ops.while_loop(loop_condition, loop_body, (i0,))
    self.evaluate(variables.global_variables_initializer())
    self.assertEqual(4, self.evaluate(r))
    self.assertAllClose(65536.0, self.evaluate(v))
