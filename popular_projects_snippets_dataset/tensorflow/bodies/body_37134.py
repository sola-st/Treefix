# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    x = constant_op.constant(3.0, name="x")
    y = constant_op.constant(2.0, name="y")

    c = lambda x, y: math_ops.less(x, 100.0)

    def b(x, y):
        y1 = math_ops.add(x, y)
        x1 = math_ops.multiply(x, y1)
        exit((x1, y1))

    rx, ry = control_flow_ops.while_loop(c, b, [x, y], parallel_iterations=1)

    r = gradients_impl.gradients([rx, ry], x)
    self.assertAllClose(304.0, r[0])
    r = gradients_impl.gradients([rx, ry], y)
    self.assertAllClose(124.0, r[0])
    r = gradients_impl.gradients([rx], x)
    self.assertAllClose(295.0, r[0])
    r = gradients_impl.gradients([rx], y)
    self.assertAllClose(120.0, r[0])
