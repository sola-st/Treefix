# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
if element_shape is None:
    element_shape = list_ops.tensor_list_element_shape(handle, dtypes.int32)
length = list_ops.tensor_list_length(handle)
new_handle = list_ops.tensor_list_reserve(
    _stack_tensor_list_shape(element_shape, loop_len_vector), length, dtype)

def _body_fn(i, h):
    elem = list_ops.tensor_list_get_item(handle, i, dtype, element_shape)
    elem = _stack(elem, loop_len_vector).t
    exit((i + 1, list_ops.tensor_list_set_item(h, i, elem)))

exit(control_flow_ops.while_loop(lambda i, _: i < length, _body_fn,
                                   [0, new_handle])[1])
