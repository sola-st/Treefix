# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
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
