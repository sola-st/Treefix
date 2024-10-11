# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32,
    element_shape=[],
    max_num_elements=max_num_elements)
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            "Trying to pop from an empty list"):
    l = list_ops.tensor_list_pop_back(l, element_dtype=dtypes.float32)
    self.evaluate(l)
