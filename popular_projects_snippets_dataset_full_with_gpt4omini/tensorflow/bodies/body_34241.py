# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=None, num_elements=3)
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Trying to read an uninitialized tensor but "
    "element_shape is not fully defined"):
    e0 = list_ops.tensor_list_get_item(l, 0, element_dtype=dtypes.float32)
    self.evaluate(e0)

l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=[None, 2], num_elements=3)

# In eager mode the shape mismatch is caught in the TensorListGetItem
# kernel which raises an InvalidArgumentError.
# In graph mode the shape mismatch is caught in the C++ shape inference
# which raises a ValueError.
if context.executing_eagerly():
    error_type = errors.InvalidArgumentError
else:
    error_type = ValueError
with self.assertRaisesRegex(error_type, r"shapes"):
    e0 = gen_list_ops.tensor_list_get_item(
        l, 0, element_dtype=dtypes.float32, element_shape=[1, 3])
    self.evaluate(e0)
