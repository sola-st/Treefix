# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    i = constant_op.constant(0, name="i")
    x = constant_op.constant(2.0, name="x")

    c = lambda i, x: math_ops.less(i, 5)

    def b(i, x):
        x = math_ops.multiply(x, 2.0)
        i = math_ops.add(i, 1)
        exit((i, x))

    _, r1 = control_flow_ops.while_loop(c, b, [i, x], parallel_iterations=1)
    _, r2 = control_flow_ops.while_loop(c, b, [i, x], parallel_iterations=1)
    rx = math_ops.add(r1, r2)

    r = gradients_impl.gradients([rx], x)
    self.assertAllClose(64.0, r[0])
