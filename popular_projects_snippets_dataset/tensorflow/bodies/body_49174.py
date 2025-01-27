# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""RNN step function.

        Args:
            time: Current timestep value.
            output_ta_t: TensorArray.
            prev_output: tuple of outputs from time - 1.
            *states: List of states.

        Returns:
            Tuple: `(time + 1, output_ta_t, output) + tuple(new_states)`
        """
current_input = tuple(ta.read(time) for ta in input_ta)
# maybe set shape.
current_input = nest.pack_sequence_as(inputs, current_input)
mask_t = masking_fn(time)
output, new_states = step_function(current_input,
                                   tuple(states) + tuple(constants))
# mask output
flat_output = nest.flatten(output)
flat_mask_output = (flat_zero_output if zero_output_for_mask
                    else nest.flatten(prev_output))
flat_new_output = compute_masked_output(mask_t, flat_output,
                                        flat_mask_output)

# mask states
flat_state = nest.flatten(states)
flat_new_state = nest.flatten(new_states)
for state, new_state in zip(flat_state, flat_new_state):
    if isinstance(new_state, ops.Tensor):
        new_state.set_shape(state.shape)
flat_final_state = compute_masked_output(mask_t, flat_new_state,
                                         flat_state)
new_states = nest.pack_sequence_as(new_states, flat_final_state)

output_ta_t = tuple(
    ta.write(time, out)
    for ta, out in zip(output_ta_t, flat_new_output))
exit((time + 1, output_ta_t,
        tuple(flat_new_output)) + tuple(new_states))
