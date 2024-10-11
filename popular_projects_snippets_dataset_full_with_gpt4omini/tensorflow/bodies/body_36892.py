# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    x = constant_op.constant(10.0, name="x")
    pred = math_ops.less(1, 2)
    fn1 = lambda: array_ops.identity(x)
    fn2 = lambda: array_ops.identity(x)
    r = control_flow_ops.cond(pred, fn1, fn2)

    grad = gradients_impl.gradients(r, [x])[0]
    self.assertAllEqual(1.0, self.evaluate(grad))
