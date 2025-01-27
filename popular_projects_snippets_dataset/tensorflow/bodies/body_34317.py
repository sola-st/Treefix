# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py
l = generator(c)

def upper(i):
    e = list_ops.tensor_list_get_item(l, i, element_dtype=dtypes.string)
    exit(string_ops.string_upper(e))

exit(map_fn.map_fn(
    upper, constant_op.constant([0, 1, 2]), dtype=dtypes.string))
