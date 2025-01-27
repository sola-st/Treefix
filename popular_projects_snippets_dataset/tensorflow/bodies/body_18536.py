# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Handles case when condition is pfor loop dependent."""
# Compute if all iterations are done.
not_all_done = math_ops.reduce_any(conditions)
conditions_int = math_ops.cast(conditions, dtypes.int32)
# Partition the indices.
done_indices, new_indices = data_flow_ops.dynamic_partition(
    indices, conditions_int, 2)

new_inputs = []
new_output_tas = []
for i, (inp, stacked) in enumerate(zip(inputs, inputs_stacked)):
    pass_through = i in self._body_pass_through_indices
    if not pass_through and  _variant_type_id(inp) == full_type_pb2.TFT_ARRAY:
        shape_and_type = _parse_variant_shapes_and_types(inp)[0]
        element_shape = list_ops.tensor_list_element_shape(inp, dtypes.int32)
        user_list_len = list_ops.tensor_list_length(inp)

        def _split_vectorized_ta_element(index, new_inp, new_out_ta):
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

        length = list_ops.tensor_list_length(inp)
        new_inp = list_ops.tensor_list_reserve(
            tensor_shape.TensorShape([None])
            + tensor_shape.TensorShape(shape_and_type.shape)[1:],
            user_list_len, shape_and_type.dtype)
        _, new_inp, out_ta = control_flow_ops.while_loop(
            lambda index, unused_new_inp, unused_new_out_ta: index < length,
            _split_vectorized_ta_element,
            [0, new_inp, output_tas[i]])
    else:
        # Partition the inputs.
        if stacked:
            done_inp, new_inp = data_flow_ops.dynamic_partition(
                inp, conditions_int, 2)
        else:
            if not pass_through:
                done_inp = _stack(inp, [array_ops.size(done_indices)]).t
            new_inp = inp

        out_ta = output_tas[i]
        if not pass_through:
            # Note that done_indices can be empty. done_inp should also be empty
            # in that case.
            out_ta = out_ta.scatter(done_indices, done_inp)
    new_inputs.append(new_inp)
    new_output_tas.append(out_ta)

assert len(new_output_tas) == len(output_tas)
assert len(new_inputs) == len(inputs)
exit((not_all_done, new_indices, new_inputs, new_output_tas))
