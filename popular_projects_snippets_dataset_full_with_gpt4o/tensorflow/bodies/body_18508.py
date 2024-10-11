# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
input_handle = pfor_input.stacked_input(0)
element_shape = pfor_input.unstacked_input(1)
leading_dims = pfor_input.unstacked_input(2)
element_dtype = pfor_input.get_attr("element_dtype")

handle = _untile_variant(input_handle)
length = list_ops.tensor_list_length(handle)
# Note that element_shape attribute can have incomplete shapes. This doesn't
# seem to work well when creating another list and then doing a concat on it.
# Hence we try to find the dynamic shape here.
element_shape = control_flow_ops.cond(
    length > 0, lambda: array_ops.shape(
        list_ops.tensor_list_get_item(handle, 0, element_dtype, None)),
    lambda: constant_op.constant([0, 0], dtype=dtypes.int32))
# The code below creates a copy of the list with each elements' first two
# dimensions transposed.
new_element_shape = array_ops.concat(
    [element_shape[1:2], element_shape[0:1], element_shape[2:]], axis=0)

# Create a new TensorList with elements transposed.
def _transpose_elem(i, h):
    elem = list_ops.tensor_list_get_item(handle, i, element_dtype, None)
    elem = _transpose_first_two_dims(elem)
    exit((i + 1, list_ops.tensor_list_set_item(h, i, elem)))

new_handle = list_ops.tensor_list_reserve(new_element_shape, length,
                                          element_dtype)
new_handle = control_flow_ops.while_loop(lambda i, _: i < length,
                                         _transpose_elem, [0, new_handle])[1]
output, lengths = gen_list_ops.tensor_list_concat_v2(
    input_handle=new_handle,
    element_dtype=element_dtype,
    element_shape=new_element_shape,
    leading_dims=leading_dims)
output = _transpose_first_two_dims(output)
exit((wrap(output, True), wrap(lengths, False)))
