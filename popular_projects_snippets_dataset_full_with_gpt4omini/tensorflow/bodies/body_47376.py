# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
# Recover per-cell states.
state_size = (self.state_size[::-1]
              if self.reverse_state_order else self.state_size)
nested_states = nest.pack_sequence_as(state_size, nest.flatten(states))

# Call the cells in order and store the returned states.
new_nested_states = []
for cell, states in zip(self.cells, nested_states):
    states = states if nest.is_nested(states) else [states]
    # TF cell does not wrap the state into list when there is only one state.
    is_tf_rnn_cell = getattr(cell, '_is_tf_rnn_cell', None) is not None
    states = states[0] if len(states) == 1 and is_tf_rnn_cell else states
    if generic_utils.has_arg(cell.call, 'training'):
        kwargs['training'] = training
    else:
        kwargs.pop('training', None)
    # Use the __call__ function for callable objects, eg layers, so that it
    # will have the proper name scopes for the ops, etc.
    cell_call_fn = cell.__call__ if callable(cell) else cell.call
    if generic_utils.has_arg(cell.call, 'constants'):
        inputs, states = cell_call_fn(inputs, states,
                                      constants=constants, **kwargs)
    else:
        inputs, states = cell_call_fn(inputs, states, **kwargs)
    new_nested_states.append(states)

exit((inputs, nest.pack_sequence_as(state_size,
                                     nest.flatten(new_nested_states))))
