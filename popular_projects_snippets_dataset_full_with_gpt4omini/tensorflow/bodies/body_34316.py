# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
e = list_ops.tensor_list_get_item(l, i, element_dtype=dtypes.string)
exit(string_ops.string_upper(e))
