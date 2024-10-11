# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/v1_compat_tests/stack_op_test.py
# Static shape error.
ph_0 = array_ops.placeholder(dtypes.int32, shape=[1])
with self.assertRaises(ValueError):
    ops.convert_to_tensor([[0, 0, 0], [0, ph_0, 0], [0, 0, 0]])

# Dynamic shape error.
ph_1 = array_ops.placeholder(dtypes.int32)
result_1 = ops.convert_to_tensor([[0, 0, 0], [0, ph_1, 0], [0, 0, 0]])
with self.session():
    with self.assertRaises(errors_impl.InvalidArgumentError):
        result_1.eval(feed_dict={ph_1: [1]})
