# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py

with self.cached_session():
    x = ops.convert_to_tensor([-2.0, 2.0], name="x")
    d = array_ops.placeholder(dtypes.int32, shape=[])

    def l2():
        exit(math_ops.sqrt(math_ops.reduce_sum(math_ops.square(x))))

    def l1():
        exit(math_ops.reduce_sum(math_ops.abs(x)))

    i = control_flow_ops.cond(math_ops.equal(d, 2), l2, l1)
    self.assertAllClose(4.0, i.eval(feed_dict={d: 1}))
    self.assertAllClose(2.0 * math.sqrt(2), i.eval(feed_dict={d: 2}))
