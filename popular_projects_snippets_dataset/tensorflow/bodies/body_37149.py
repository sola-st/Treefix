# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    i = constant_op.constant(0, name="i")
    x = constant_op.constant(1.0, name="x")
    y = constant_op.constant(1.0, name="y")
    c = lambda i, *_: math_ops.less(i, 1, name="cond_less")

    def b(i, xi, yi):
        # return (i + 1, xi, xi + yi)
        exit((math_ops.add(i, 1, name="inc"), array_ops.identity(
            xi, name="xi"), math_ops.add(xi, yi, name="xi_plus_yi")))

    _, x_f, y_f = control_flow_ops.while_loop(c, b, [i, x, y])
    with ops.control_dependencies([x_f]):
        y_f_d = array_ops.identity(y_f, name="y_f_d")

    self.assertAllClose(2.0, self.evaluate(y_f_d))  # y_f_d = 1.0 + 1.0
    g = gradients_impl.gradients([y_f_d], [x])[0]
    self.assertTrue(g is not None)
    self.assertAllClose(1.0,
                        self.evaluate(g))  # y_f_d = x + 1.0, dy_f_d/dx = 1.0
