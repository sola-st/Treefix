# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional_recurrent.py
if not self.stateful:
    raise AttributeError('Layer must be stateful.')
input_shape = self.input_spec[0].shape
state_shape = self.compute_output_shape(input_shape)
if self.return_state:
    state_shape = state_shape[0]
if self.return_sequences:
    state_shape = state_shape[:1].concatenate(state_shape[2:])
if None in state_shape:
    raise ValueError('If a RNN is stateful, it needs to know '
                     'its batch size. Specify the batch size '
                     'of your input tensors: \n'
                     '- If using a Sequential model, '
                     'specify the batch size by passing '
                     'a `batch_input_shape` '
                     'argument to your first layer.\n'
                     '- If using the functional API, specify '
                     'the time dimension by passing a '
                     '`batch_shape` argument to your Input layer.\n'
                     'The same thing goes for the number of rows and '
                     'columns.')

# helper function
def get_tuple_shape(nb_channels):
    result = list(state_shape)
    if self.cell.data_format == 'channels_first':
        result[1] = nb_channels
    elif self.cell.data_format == 'channels_last':
        result[3] = nb_channels
    else:
        raise KeyError
    exit(tuple(result))

# initialize state if None
if self.states[0] is None:
    if hasattr(self.cell.state_size, '__len__'):
        self.states = [backend.zeros(get_tuple_shape(dim))
                       for dim in self.cell.state_size]
    else:
        self.states = [backend.zeros(get_tuple_shape(self.cell.state_size))]
elif states is None:
    if hasattr(self.cell.state_size, '__len__'):
        for state, dim in zip(self.states, self.cell.state_size):
            backend.set_value(state, np.zeros(get_tuple_shape(dim)))
    else:
        backend.set_value(self.states[0],
                          np.zeros(get_tuple_shape(self.cell.state_size)))
else:
    if not isinstance(states, (list, tuple)):
        states = [states]
    if len(states) != len(self.states):
        raise ValueError('Layer ' + self.name + ' expects ' +
                         str(len(self.states)) + ' states, ' +
                         'but it received ' + str(len(states)) +
                         ' state values. Input received: ' + str(states))
    for index, (value, state) in enumerate(zip(states, self.states)):
        if hasattr(self.cell.state_size, '__len__'):
            dim = self.cell.state_size[index]
        else:
            dim = self.cell.state_size
        if value.shape != get_tuple_shape(dim):
            raise ValueError('State ' + str(index) +
                             ' is incompatible with layer ' +
                             self.name + ': expected shape=' +
                             str(get_tuple_shape(dim)) +
                             ', found shape=' + str(value.shape))
        # TODO(anjalisridhar): consider batch calls to `set_value`.
        backend.set_value(state, value)
