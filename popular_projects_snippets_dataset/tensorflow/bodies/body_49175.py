# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""RNN step function.

        Args:
            time: Current timestep value.
            output_ta_t: TensorArray.
            *states: List of states.

        Returns:
            Tuple: `(time + 1,output_ta_t) + tuple(new_states)`
        """
current_input = tuple(ta.read(time) for ta in input_ta)
current_input = nest.pack_sequence_as(inputs, current_input)
output, new_states = step_function(current_input,
                                   tuple(states) + tuple(constants))
flat_state = nest.flatten(states)
flat_new_state = nest.flatten(new_states)
for state, new_state in zip(flat_state, flat_new_state):
    if isinstance(new_state, ops.Tensor):
        new_state.set_shape(state.shape)

flat_output = nest.flatten(output)
output_ta_t = tuple(
    ta.write(time, out) for ta, out in zip(output_ta_t, flat_output))
new_states = nest.pack_sequence_as(initial_states, flat_new_state)
exit((time + 1, output_ta_t) + tuple(new_states))
