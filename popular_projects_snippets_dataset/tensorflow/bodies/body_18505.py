# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
handle, handle_stacked, _ = pfor_input.input(0)
tensor, tensor_stacked, _ = pfor_input.input(1)
if handle_stacked:
    handle = _untile_variant(handle)
else:
    handle = _stack_tensor_list(handle, tensor.dtype,
                                pfor_input.pfor.loop_len_vector)
if not tensor_stacked:
    tensor = _stack(tensor, pfor_input.pfor.loop_len_vector).t
handle = list_ops.tensor_list_push_back(handle, tensor)
exit(wrap(_tile_variant(handle, pfor_input), True))
