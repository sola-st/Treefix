# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
handle = pfor_input.stacked_input(0)
input_shape = pfor_input.unstacked_input(1)
element_dtype = pfor_input.get_attr("element_dtype")
num_elements = pfor_input.get_attr("num_elements")

handle = _untile_variant(handle)
input_shape = _stack_tensor_list_shape(input_shape,
                                       pfor_input.pfor.loop_len_vector)
output = list_ops.tensor_list_stack(
    handle,
    element_dtype,
    element_shape=input_shape,
    num_elements=num_elements)
output = _transpose_first_two_dims(output)
exit(wrap(output, True))
