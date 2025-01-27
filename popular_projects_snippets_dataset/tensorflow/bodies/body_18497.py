# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
element_shape = pfor_input.unstacked_input(0)
num_elements = pfor_input.unstacked_input(1)
element_dtype = pfor_input.get_attr("element_dtype")

# Prepend a dimension to element_shape.
element_shape = _stack_tensor_list_shape(element_shape,
                                         pfor_input.pfor.loop_len_vector)
handle = list_ops.tensor_list_reserve(
    element_shape, num_elements, element_dtype=element_dtype)

exit(wrap(_tile_variant(handle, pfor_input), True))
