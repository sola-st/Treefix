# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Create arguments passed to converted while_loop."""
loop_len = self._pfor.loop_len_vector[0]
inputs = []
# TensorArrays for outputs of converted while loop
output_tas = []

with ops.name_scope("while_init"):
    for inp in self._pfor_input.inputs:
        inputs.append(inp.t)
        variant_type_id = _variant_type_id(inp.t)
        if variant_type_id in _INTERNAL_STACKING_TYPE_IDS:
            if variant_type_id != full_type_pb2.TFT_ARRAY:
                raise NotImplementedError(
                    "While loop conversion is only supported for TensorLists. Got "
                    f"another variant {inp.t}, probably an optional. Please file "
                    "a bug.")

            # For TensorLists, the input format is:
            #
            #   List[user_list_len, Tensor[loop_len, ...]]
            #
            # rather than the usual
            #
            #   Tensor[loop_len, ...]
            #
            # The body of the loop will take and return lists in this "internal
            # vectorization" format, so we want to keep it that way as much as
            # possible. We'll accumulate finished iterations (only relevant for
            # pfor-loop-variant while_loop conditions) in an accumulator with
            # type :
            #
            #   List[user_list_len, List[loop_len, Tensor[...]]]
            #
            # This means that each while_loop iteration, we'll iterate over the
            # length of the TensorList, dividing done/remaining pfor loop indices
            # and scattering the done indices into the inner nested list of the
            # accumulator.
            element_shape = list_ops.tensor_list_element_shape(
                inp.t, dtypes.int32)
            if inp.is_stacked:
                # Shapes may be tf.constant(-1) for fully dynamic, in which case
                # slicing is an error.
                element_shape = control_flow_ops.cond(
                    math_ops.equal(array_ops.rank(element_shape), 0),
                    lambda: element_shape,
                    lambda: element_shape[1:])
            dtype = _parse_variant_shapes_and_types(inp.t)[0].dtype

            def _init_loop_body(index, output_ta):
                output_ta = output_ta.write(
                    index,
                    list_ops.tensor_list_reserve(element_shape, loop_len, dtype))
                exit((index + 1, output_ta))

            length = list_ops.tensor_list_length(inp.t)
            output_ta = tensor_array_ops.TensorArray(
              inp.t.dtype,  # Variant; this is a nested TensorList
              size=length,
              dynamic_size=True,
              infer_shape=False)
            _, output_ta = control_flow_ops.while_loop(
                lambda index, _: index < length,
                _init_loop_body,
                [0, output_ta])
        else:
            output_ta = tensor_array_ops.TensorArray(
              inp.t.dtype,
              size=loop_len,
              dynamic_size=False,
              infer_shape=True)
        output_tas.append(output_ta)
    # See documentation for __call__ for the structure of init_values.
indices = (
    math_ops.range(self._pfor.loop_len_vector[0])
    if self._pfor.all_indices_partitioned else self._pfor.all_indices)
exit([True, indices] + inputs + output_tas)
