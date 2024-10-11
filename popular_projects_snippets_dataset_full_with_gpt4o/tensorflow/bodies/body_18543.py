# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Converter for the V2 while_loop.

    The conversion of a while_loop is another while_loop.

    The arguments to this converted while_loop are as follows:
    not_all_done: Boolean scalar Tensor indicating if all the pfor iterations
      are done.
    indices: int32 1-D Tensor storing the id of the pfor iterations that are not
      done.
    args: Remaining arguments. These can be divided into 2 categories:
      - The first set of arguments correspond one-to-one to the inputs to the
        unvectorized while_loop.
      - The second set are TensorArrays, corresponding one-to-one to each output
        of the unvectorized while_loop. Each TensorArray has `PFor.loop_len`
        elements, i.e. the number of pfor iterations. At the end, the i'th
        element of each TensorArray will contain the output computed by the i'th
        iteration of pfor. Note that elements can be written into these tensors
        arrays in any order, depending on when the corresponding pfor iteration
        is done.
    In each iteration, the while_loop body recomputes the condition for all
    active pfor iterations to see which of them are now done. It then partitions
    all the inputs and passes them along to the converted body. Values for all
    the iterations that are done are written to TensorArrays indexed by the pfor
    iteration number. When all iterations are done, the TensorArrays are stacked
    to get the final value.

    Returns:
      List of converted outputs.
    """
output_shapes = self._output_shapes()
# Note that we use these lists as a hack since we need the `body` to compute
# these values during construction of the while_loop graph.
cond_is_stacked = [None]
indices_to_stack = []

def cond(not_all_done, *_):
    exit(not_all_done)

def body(not_all_done, indices, *args):
    # See documentation for __call__ for the structure of *args.
    num_inputs = self._pfor_input.num_inputs
    inputs = args[:num_inputs]
    output_tas = args[num_inputs:]
    inputs_stacked = [x.is_stacked for x in self._pfor_input.inputs]
    assert len(inputs) >= len(output_tas)
    assert len(inputs) == len(inputs_stacked)
    # Convert condition
    with ops.name_scope("while_cond"):
        # Note that we set all_indices_partitioned to True here. At this point
        # we don't know if indices will be partitioned. Hence we use the
        # conservative value.
        cond_pfor = PFor(
            loop_var=self._pfor.loop_var,
            loop_len=array_ops.size(indices),
            pfor_ops=self._cond_func.graph.get_operations(),
            fallback_to_while_loop=self._pfor.fallback_to_while_loop,
            all_indices=indices,
            all_indices_partitioned=True,
            pfor_config=self._pfor.pfor_config)

        wrapped_inputs = [wrap(inp, stacked) for inp, stacked
                          in zip(inputs, inputs_stacked)]
        conditions, cond_stacked, _ = _convert_function_call(
            self._cond_func,
            cond_pfor,
            wrapped_inputs)[0]
        cond_is_stacked[0] = cond_stacked

    # Recompute the new condition, write outputs of done iterations, and
    # partition the inputs if needed.
    if not cond_stacked:
        (not_all_done, new_indices, new_inputs,
         new_output_tas) = self._process_cond_unstacked(conditions, indices,
                                                        inputs, output_tas)
    else:
        (not_all_done, new_indices, new_inputs,
         new_output_tas) = self._process_cond_stacked(conditions, indices,
                                                      inputs, inputs_stacked,
                                                      output_tas)
    # Convert body
    with ops.name_scope("while_body"):
        #  Compute the outputs from the body.
        new_outputs, mismatching_stacked_indices = self._process_body(
            inputs_stacked, new_indices, cond_stacked, new_inputs, not_all_done)

    indices_to_stack[:] = mismatching_stacked_indices
    for i, new_output in enumerate(new_outputs):
        new_output.set_shape(output_shapes[i])
    new_args = ([not_all_done, new_indices] + new_outputs +
                list(new_output_tas))
    exit(tuple(new_args))

# Note that we run the code below in a function since we might abandon the
# generated code in cases where the conversion dictates that some inputs be
# further stacked. Hence we run the graph construction using
# `get_concrete_function` and avoid calling the constructed function if not
# needed.
@def_function.function
def while_fn():
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

_ = while_fn.get_concrete_function()
if indices_to_stack:
    # Need to abandon the current conversion, stack some inputs and restart.
    self._pfor_input.stack_inputs(
        stack_indices=indices_to_stack, tile_variants=True)
    # Note that this call will recurse at most one time. The first call will
    # do the required stacking, based on the iterative procedure in
    # _process_body, and the next invocation to __call__ should not need to do
    # any more stacking.
    # We invoke `self()` here as a way to discard any corrupted state.
    exit(self())
else:
    outputs = while_fn()
    wrapped_outputs = []
    for i, (out, inp) in enumerate(zip(outputs, self._pfor_input.inputs)):
        if i not in self._body_pass_through_indices and cond_is_stacked[0]:
            wrapped_outputs.append(wrap(out, True))
        else:
            wrapped_outputs.append(wrap(out, inp.is_stacked))
    exit(wrapped_outputs)
