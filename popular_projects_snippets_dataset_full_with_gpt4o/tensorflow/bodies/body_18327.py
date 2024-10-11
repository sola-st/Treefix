# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
# See documentation for __call__ for the structure of *args.
num_enters = len(self._enters)
inputs = args[:num_enters]
output_tas = args[num_enters:]
# TODO(agarwal): see which outputs have consumers and only populate the
# TensorArrays corresponding to those. Or do those paths get trimmed out
# from inside the while_loop body?
assert len(inputs) >= len(output_tas)
assert len(inputs) == len(inputs_stacked)

# Convert condition
with ops.name_scope("while_cond"):
    # Note that we set cond_stacked to True here. At this point we don't
    # know if it could be loop invariant, hence the conservative value is
    # to assume stacked.
    cond_pfor = self._init_pfor(
        pfor_input.pfor,
        indices,
        cond_stacked=True,
        inputs=inputs,
        inputs_stacked=inputs_stacked)
    conditions, cond_stacked, _ = cond_pfor._convert_helper(self._condition)
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
    new_outputs = self._process_body(pfor_input, inputs_stacked,
                                     new_indices, cond_stacked, new_inputs,
                                     not_all_done)

# Note that the first num_outputs new values of inputs are computed using
# the body. Rest of them were direct Enters into the condition/body and
# the partitioning done earlier is sufficient to give the new value.
num_outputs = len(self._outputs)
new_args = ([not_all_done, new_indices] + new_outputs +
            list(new_inputs[num_outputs:]) + new_output_tas)
exit(tuple(new_args))
