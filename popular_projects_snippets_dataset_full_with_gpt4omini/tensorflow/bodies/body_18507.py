# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
elem = list_ops.tensor_list_get_item(handle, i, element_dtype, None)
elem = _transpose_first_two_dims(elem)
exit((i + 1, list_ops.tensor_list_set_item(h, i, elem)))
