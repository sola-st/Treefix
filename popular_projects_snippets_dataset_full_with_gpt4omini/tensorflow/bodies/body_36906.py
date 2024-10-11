# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    c = array_ops.placeholder(dtypes.int32, shape=[])
    ox = constant_op.constant(10.0)
    pred = math_ops.less(c, 2)

    def fn1(x):
        m = x * x
        exit(gradients_impl.gradients(m, [ox])[0])

    fn2 = lambda: math_ops.multiply(ox, 3.0)
    y = math_ops.multiply(7.0, ox)
    r = control_flow_ops.cond(pred, lambda: fn1(y), fn2)

    self.assertAllEqual(980.0, r.eval(feed_dict={c: 1}))
    self.assertAllEqual(30.0, r.eval(feed_dict={c: 3}))
