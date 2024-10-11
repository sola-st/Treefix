# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = list_ops.empty_tensor_list(
    element_dtype=dtypes.float32, element_shape=element_shape)
exit(list_ops.tensor_list_concat(l, element_dtype=dtypes.float32))
