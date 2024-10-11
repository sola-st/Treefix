# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
"""Take a time step of the dynamic RNN.

    Args:
      time: int32 scalar Tensor.
      output_ta_t: List of `TensorArray`s that represent the output.
      state: nested tuple of vector tensors that represent the state.

    Returns:
      The tuple (time + 1, output_ta_t with updated flow, new_state).
    """

if in_graph_mode:
    input_t = tuple(ta.read(time) for ta in input_ta)
    # Restore some shape information
    for input_, shape in zip(input_t, inputs_got_shape):
        input_.set_shape(shape[1:])
else:
    input_t = tuple(ta[time.numpy()] for ta in input_ta)

input_t = nest.pack_sequence_as(structure=inputs, flat_sequence=input_t)
# Keras RNN cells only accept state as list, even if it's a single tensor.
call_cell = lambda: cell(input_t, state)

if sequence_length is not None:
    (output, new_state) = _rnn_step(
        time=time,
        sequence_length=sequence_length,
        min_sequence_length=min_sequence_length,
        max_sequence_length=max_sequence_length,
        zero_output=zero_output,
        state=state,
        call_cell=call_cell,
        state_size=state_size,
        skip_conditionals=True)
else:
    (output, new_state) = call_cell()

# Pack state if using state tuples
output = nest.flatten(output)

if in_graph_mode:
    output_ta_t = tuple(
        ta.write(time, out) for ta, out in zip(output_ta_t, output))
else:
    for ta, out in zip(output_ta_t, output):
        ta[time.numpy()] = out

exit((time + 1, output_ta_t, new_state))
