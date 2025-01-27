# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
tensor = pfor_input.stacked_input(0)
element_shape = pfor_input.unstacked_input(1)
tensor = _transpose_first_two_dims(tensor)
element_shape = _stack_tensor_list_shape(element_shape,
                                         pfor_input.pfor.loop_len_vector)
handle = list_ops.tensor_list_from_tensor(tensor, element_shape)
exit(wrap(_tile_variant(handle, pfor_input), True))
