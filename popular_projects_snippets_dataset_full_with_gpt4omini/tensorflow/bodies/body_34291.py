# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=None, num_elements=3)
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    r"Trying to concat list with only uninitialized tensors "
    r"but element_shape_except_first_dim is not fully defined"):
    t = list_ops.tensor_list_concat(l, element_dtype=dtypes.float32)
    self.evaluate(t)
