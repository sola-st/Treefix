# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    data = array_ops.placeholder(dtypes.float32, shape=[])
    enter_1 = gen_control_flow_ops.enter(data, "foo_1", False)
    enter_2 = gen_control_flow_ops.enter(data, "foo_2", False)
    res = math_ops.add(enter_1, enter_2)
    with self.assertRaisesOpError("has inputs from different frames"):
        res.eval(feed_dict={data: 1.0})
