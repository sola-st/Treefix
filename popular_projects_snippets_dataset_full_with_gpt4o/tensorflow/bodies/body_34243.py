# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32, element_shape=[], max_num_elements=3)
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Trying to modify element 0 in a list with 0 elements."):
    l = list_ops.tensor_list_set_item(l, 0, 1.)
    self.evaluate(l)
