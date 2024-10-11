# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
elem = list_ops.tensor_list_get_item(handle, i, dtype, element_shape)
elem = _stack(elem, loop_len_vector).t
exit((i + 1, list_ops.tensor_list_set_item(h, i, elem)))
