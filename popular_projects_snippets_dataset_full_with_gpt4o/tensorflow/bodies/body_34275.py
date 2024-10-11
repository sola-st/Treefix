# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l1 = list_ops.tensor_list_reserve(
    element_shape=[], element_dtype=dtypes.float32, num_elements=2)
l2 = list_ops.tensor_list_reserve(
    element_shape=[], element_dtype=dtypes.float32, num_elements=3)
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Trying to add two lists of tensors with different lengths"):
    l = math_ops.add_n([l1, l2])
    self.evaluate(list_ops.tensor_list_stack(l, element_dtype=dtypes.float32))
