# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
with self.cached_session():
    data = constant_op.constant([1, 2, 3, 4, 5, 6], name="data")
    zero = ops.convert_to_tensor(0)
    one = ops.convert_to_tensor(1)
    less_op = math_ops.less(zero, one)
    switch_op = control_flow_ops.switch(data, less_op)
    merge_op = control_flow_ops.merge(switch_op)[0]

    result = self.evaluate(merge_op)
self.assertAllEqual(np.arange(1, 7), result)
