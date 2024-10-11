# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.tensor_list_split(
    input_tensor, element_shape=None, lengths=lengths)
self.assertAllEqual(
    list_ops.tensor_list_stack(l, element_dtype=dtypes.float32),
    expected_stacked_output)
