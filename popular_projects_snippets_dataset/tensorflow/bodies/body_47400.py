# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
"""Reset the recorded states for the stateful RNN layer.

    Can only be used when RNN layer is constructed with `stateful` = `True`.
    Args:
      states: Numpy arrays that contains the value for the initial state, which
        will be feed to cell at the first time step. When the value is None,
        zero filled numpy array will be created based on the cell state size.

    Raises:
      AttributeError: When the RNN layer is not stateful.
      ValueError: When the batch size of the RNN layer is unknown.
      ValueError: When the input numpy array is not compatible with the RNN
        layer state, either size wise or dtype wise.
    """
if not self.stateful:
    raise AttributeError('Layer must be stateful.')
spec_shape = None
if self.input_spec is not None:
    spec_shape = nest.flatten(self.input_spec[0])[0].shape
if spec_shape is None:
    # It is possible to have spec shape to be None, eg when construct a RNN
    # with a custom cell, or standard RNN layers (LSTM/GRU) which we only know
    # it has 3 dim input, but not its full shape spec before build().
    batch_size = None
else:
    batch_size = spec_shape[1] if self.time_major else spec_shape[0]
if not batch_size:
    raise ValueError('If a RNN is stateful, it needs to know '
                     'its batch size. Specify the batch size '
                     'of your input tensors: \n'
                     '- If using a Sequential model, '
                     'specify the batch size by passing '
                     'a `batch_input_shape` '
                     'argument to your first layer.\n'
                     '- If using the functional API, specify '
                     'the batch size by passing a '
                     '`batch_shape` argument to your Input layer.')
# initialize state if None
if nest.flatten(self.states)[0] is None:
    if getattr(self.cell, 'get_initial_state', None):
        flat_init_state_values = nest.flatten(self.cell.get_initial_state(
            inputs=None, batch_size=batch_size,
            dtype=self.dtype or backend.floatx()))
    else:
        flat_init_state_values = nest.flatten(_generate_zero_filled_state(
            batch_size, self.cell.state_size, self.dtype or backend.floatx()))
    flat_states_variables = nest.map_structure(
        backend.variable, flat_init_state_values)
    self.states = nest.pack_sequence_as(self.cell.state_size,
                                        flat_states_variables)
    if not nest.is_nested(self.states):
        self.states = [self.states]
elif states is None:
    for state, size in zip(nest.flatten(self.states),
                           nest.flatten(self.cell.state_size)):
        backend.set_value(
            state,
            np.zeros([batch_size] + tensor_shape.TensorShape(size).as_list()))
else:
    flat_states = nest.flatten(self.states)
    flat_input_states = nest.flatten(states)
    if len(flat_input_states) != len(flat_states):
        raise ValueError('Layer ' + self.name + ' expects ' +
                         str(len(flat_states)) + ' states, '
                         'but it received ' + str(len(flat_input_states)) +
                         ' state values. Input received: ' + str(states))
    set_value_tuples = []
    for i, (value, state) in enumerate(zip(flat_input_states,
                                           flat_states)):
        if value.shape != state.shape:
            raise ValueError(
                'State ' + str(i) + ' is incompatible with layer ' +
                self.name + ': expected shape=' + str(
                    (batch_size, state)) + ', found shape=' + str(value.shape))
        set_value_tuples.append((state, value))
    backend.batch_set_value(set_value_tuples)
