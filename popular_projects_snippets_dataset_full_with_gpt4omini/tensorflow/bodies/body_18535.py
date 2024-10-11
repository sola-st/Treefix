# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
elem = list_ops.tensor_list_get_item(inp, index, shape_and_type.dtype,
                                     element_shape)
if stacked:
    done_elem, new_elem = data_flow_ops.dynamic_partition(
        elem, conditions_int, 2)
    new_inp = list_ops.tensor_list_set_item(new_inp, index, new_elem)
else:
    done_elem = _stack(elem, [array_ops.size(done_indices)]).t
done_accum = new_out_ta.read(index)
done_accum = list_ops.tensor_list_scatter(
    tensor=done_elem, indices=done_indices, input_handle=done_accum)
new_out_ta = new_out_ta.write(index, done_accum)
exit((index + 1, new_inp, new_out_ta))
