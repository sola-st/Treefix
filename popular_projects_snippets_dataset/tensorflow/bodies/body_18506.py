# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
handle = pfor_input.stacked_input(0)
element_shape = pfor_input.unstacked_input(1)
handle = _untile_variant(handle)

if element_shape.shape.ndims == 0:
    # Default / unspecified
    vectorized_shape = -1
else:
    # PopBack has an element shape set when it's the gradient of PushBack, only
    # used when the list is uninitialized.
    vectorized_shape = array_ops.concat(
        [pfor_input.pfor.loop_len_vector, element_shape], axis=0)

output_handle, tensor = gen_list_ops.tensor_list_pop_back(
    input_handle=handle, element_dtype=pfor_input.get_attr("element_dtype"),
    element_shape=vectorized_shape)
exit((wrap(output_handle, True), wrap(tensor, True)))
