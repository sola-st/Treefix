# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    x = constant_op.constant(10.0, name="x")
    pred = math_ops.less(1, 2)

    def true_fn():
        a = x * x
        exit(a * a)

    def false_fn():
        exit(x * x)

    r = control_flow_ops.cond(pred, true_fn, false_fn)

    self.assertAllEqual(r, 10000.)
    grad = gradients_impl.gradients(r, [x])[0]
    self.assertAllEqual(grad, 4000.)
