# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    c = array_ops.placeholder(dtypes.int32, shape=[])
    x = constant_op.constant(10.0)
    pred = math_ops.less(c, 2)
    fn1 = lambda: math_ops.multiply(x, 42.0)
    fn2 = lambda: math_ops.multiply(x, 3.0)
    r = control_flow_ops.cond(pred, fn1, fn2)

    grad = gradients_impl.gradients(r, [x])[0]
    self.assertAllEqual(42.0, grad.eval(feed_dict={c: 1}))
    self.assertAllEqual(3.0, grad.eval(feed_dict={c: 3}))
