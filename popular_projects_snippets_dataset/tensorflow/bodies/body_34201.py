# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=None, num_elements=3)
with self.assertRaisesRegex(
    errors.InvalidArgumentError, "Tried to stack list which only contains "
    "uninitialized tensors and has a "
    "non-fully-defined element_shape: <unknown>"):
    t = list_ops.tensor_list_stack(l, element_dtype=dtypes.float32)
    self.evaluate(t)
