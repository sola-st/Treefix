# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    v = constant_op.constant(2.0, name="v")
    c = lambda v: math_ops.less(v, 100.0)
    b = math_ops.square
    r = control_flow_ops.while_loop(c, b, [v], parallel_iterations=1)
    r = control_flow_ops.cond(math_ops.less(1, 2), lambda: r, lambda: v)

    r = gradients_impl.gradients(r, v)[0]
    self.assertAllClose(1024.0, self.evaluate(r))
