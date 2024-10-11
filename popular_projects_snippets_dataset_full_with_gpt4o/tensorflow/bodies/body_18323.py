# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
num_outputs = len(self._outputs)
# Compute if all iterations are done.
not_all_done = math_ops.reduce_any(conditions)
conditions_int = math_ops.cast(conditions, dtypes.int32)
# Partition the indices.
done_indices, new_indices = data_flow_ops.dynamic_partition(
    indices, conditions_int, 2)

new_inputs = []
new_output_tas = []
for i, (inp, stacked) in enumerate(zip(inputs, inputs_stacked)):
    # Partition the inputs.
    if stacked:
        done_inp, new_inp = data_flow_ops.dynamic_partition(
            inp, conditions_int, 2)
    else:
        # TODO(agarwal): avoid this stacking. See TODO earlier in
        # _process_cond_unstacked.
        done_inp = _stack(inp, [array_ops.size(done_indices)]).t
        new_inp = inp
    new_inputs.append(new_inp)
    # For iterations that are done, write them to TensorArrays.
    if i < num_outputs:
        out_ta = output_tas[i]
        # Note that done_indices can be empty. done_inp should also be empty in
        # that case.
        new_output_tas.append(out_ta.scatter(done_indices, done_inp))
exit((not_all_done, new_indices, new_inputs, new_output_tas))
