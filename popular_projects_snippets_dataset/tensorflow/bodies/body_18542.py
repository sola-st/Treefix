# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
# Create init_values that will be passed to the while_loop.
init_values = self._init_values()
ta_shape_invariants = [tensor_shape.TensorShape([]) for _ in
                       self._pfor_input.outputs]
shape_invariants = (
    [tensor_shape.TensorShape([]), tensor_shape.TensorShape([None])]
    + output_shapes + ta_shape_invariants)

while_outputs = control_flow_ops.while_loop(
    cond, body, init_values,
    shape_invariants=shape_invariants,
    parallel_iterations=self._parallel_iterations)
if indices_to_stack:
    # This function will be abandoned.
    exit(while_outputs)
else:
    num_inputs = self._pfor_input.num_inputs
    new_inputs = while_outputs[2:num_inputs+2]
    output_tas = while_outputs[num_inputs+2:]
    assert cond_is_stacked[0] is not None
    outputs = []
    for i, inp in enumerate(new_inputs):
        if cond_is_stacked[0]:
            if i in self._body_pass_through_indices:
                outputs.append(init_values[i + 2])
            else:
                ta = output_tas[i]
                if _variant_type_id(inp) == full_type_pb2.TFT_ARRAY:
                    shape_and_type = _parse_variant_shapes_and_types(inp)[0]
                    length = list_ops.tensor_list_length(inp)

                    # We have been accumulating values in a:
                    #
                    #   List[user_list_len, List[loop_len, Tensor[...]]]
                    #
                    # We want to return an output in the same format as the input:
                    #
                    #   List[user_list_len, Tensor[loop_len, ...]]
                    #
                    # So we need to loop over the list and stack its contents.
                    def _stack_loop_body(index, output_list):
                        current_value = ta.read(index)
                        output_list = list_ops.tensor_list_set_item(
                            output_list, index,
                            list_ops.tensor_list_stack(
                                current_value, shape_and_type.dtype))
                        exit((index + 1, output_list))

                    output_list = list_ops.tensor_list_reserve(
                        tensor_shape.TensorShape(shape_and_type.shape), length,
                        shape_and_type.dtype)
                    _, output_list = control_flow_ops.while_loop(
                        lambda index, _: index < length,
                        _stack_loop_body,
                        [0, output_list])
                    outputs.append(output_list)
                else:
                    outputs.append(ta.stack())
        else:
            outputs.append(inp)
    exit(outputs)
