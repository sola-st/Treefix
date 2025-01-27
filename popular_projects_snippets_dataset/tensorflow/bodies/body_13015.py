# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/rnn.py
"""RNN that accepts a state saver for time-truncated RNN calculation.

  Args:
    cell: An instance of `RNNCell`.
    inputs: A length T list of inputs, each a `Tensor` of shape `[batch_size,
      input_size]`.
    state_saver: A state saver object with methods `state` and `save_state`.
    state_name: Python string or tuple of strings.  The name to use with the
      state_saver. If the cell returns tuples of states (i.e., `cell.state_size`
      is a tuple) then `state_name` should be a tuple of strings having the same
      length as `cell.state_size`.  Otherwise it should be a single string.
    sequence_length: (optional) An int32/int64 vector size [batch_size]. See the
      documentation for rnn() for more details about sequence_length.
    scope: VariableScope for the created subgraph; defaults to "rnn".

  Returns:
    A pair (outputs, state) where:
      outputs is a length T list of outputs (one for each input)
      states is the final state

  Raises:
    TypeError: If `cell` is not an instance of RNNCell.
    ValueError: If `inputs` is `None` or an empty list, or if the arity and
     type of `state_name` does not match that of `cell.state_size`.
  """
state_size = cell.state_size
state_is_tuple = nest.is_nested(state_size)
state_name_tuple = nest.is_nested(state_name)

if state_is_tuple != state_name_tuple:
    raise ValueError("Argument `state_name` should be the same type as "
                     f"`cell.state_size`. Received: state_name={state_name!s}, "
                     f"cell.state_size={state_size!s}.")

if state_is_tuple:
    state_name_flat = nest.flatten(state_name)
    state_size_flat = nest.flatten(state_size)

    if len(state_name_flat) != len(state_size_flat):
        raise ValueError("Number of elements in argument `state_name` and "
                         "`cell.state_size` are mismatched. Received "
                         f"state_name={state_name} with {len(state_name_flat)} "
                         f"elements and cell.state_size={cell.state_size} with "
                         f"{len(state_size_flat)} elements.")

    initial_state = nest.pack_sequence_as(
        structure=state_size,
        flat_sequence=[state_saver.state(s) for s in state_name_flat])
else:
    initial_state = state_saver.state(state_name)

(outputs, state) = static_rnn(
    cell,
    inputs,
    initial_state=initial_state,
    sequence_length=sequence_length,
    scope=scope)

if state_is_tuple:
    flat_state = nest.flatten(state)
    state_name = nest.flatten(state_name)
    save_state = [
        state_saver.save_state(name, substate)
        for name, substate in zip(state_name, flat_state)
    ]
else:
    save_state = [state_saver.save_state(state_name, state)]

with ops.control_dependencies(save_state):
    last_output = outputs[-1]
    flat_last_output = nest.flatten(last_output)
    flat_last_output = [
        array_ops.identity(output) for output in flat_last_output
    ]
    outputs[-1] = nest.pack_sequence_as(
        structure=last_output, flat_sequence=flat_last_output)

    if state_is_tuple:
        state = nest.pack_sequence_as(
            structure=state,
            flat_sequence=[array_ops.identity(s) for s in flat_state])
    else:
        state = array_ops.identity(state)

exit((outputs, state))
