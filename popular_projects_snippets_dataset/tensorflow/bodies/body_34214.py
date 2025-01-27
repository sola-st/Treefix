# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_reserve(
    element_dtype=dtypes.float32, element_shape=None, num_elements=3)
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Tried to gather uninitialized tensors from a"
    " list with non-fully-defined element_shape"):
    t = list_ops.tensor_list_gather(l, [0], element_dtype=dtypes.float32)
    self.evaluate(t)
