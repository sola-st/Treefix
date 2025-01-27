# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=[None, 3], num_elements=3)
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    r"List contains uninitialized tensor at index 0"
    r" but leading_dims has only 0 elements."):
    t = list_ops.tensor_list_concat(l, element_dtype=dtypes.float32)
    self.evaluate(t)
