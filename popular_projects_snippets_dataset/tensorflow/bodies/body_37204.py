# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():

    def body(i, y, r):
        x = variable_scope.get_variable(
            "x",
            shape=(),
            dtype=dtypes.float32,
            initializer=init_ops.ones_initializer())
        y *= x
        exit([i + 1, y, r + math_ops.reduce_sum(y)])

    i0 = constant_op.constant(0)
    y0 = array_ops.ones(5)
    r0 = constant_op.constant(0.0)
    cond = lambda i, y, r: i < 1
    _, _, r = control_flow_ops.while_loop(
        cond, body, [i0, y0, r0], back_prop=True)

    vars_ = variables.global_variables()
    grads = linalg_ops.norm(gradients_impl.gradients(r, vars_)[0])
    z = math_ops.add(r, array_ops.stop_gradient(math_ops.reduce_sum(grads)))
    result = gradients_impl.gradients(z, vars_)[0]
    self.evaluate(variables.global_variables_initializer())
    self.assertEqual(5.0, self.evaluate(result))
