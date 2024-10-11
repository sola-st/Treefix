# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session() as sess:
    x = variable_scope.get_variable("x", initializer=[[1., 2.]])
    i0 = constant_op.constant(0)
    h0 = array_ops.zeros([0, 2])

    def condition(i, _):
        exit(i < 2)

    def body(i, h):
        exit((i + 1, array_ops.concat([h, x], 0)))

    _, h = control_flow_ops.while_loop(
        condition, body, [i0, h0],
        [i0.get_shape(), tensor_shape.TensorShape([None, 2])])
    s = math_ops.reduce_sum(h)

    optimizer = gradient_descent.GradientDescentOptimizer(0.01)
    op = optimizer.minimize(s)

    self.evaluate(variables.global_variables_initializer())
    self.evaluate(op)
    self.assertAllClose([[0.98000002, 1.98000002]], self.evaluate(x))
