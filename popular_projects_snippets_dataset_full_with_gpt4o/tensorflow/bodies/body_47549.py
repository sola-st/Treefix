# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional_recurrent.py
# Note input_shape will be list of shapes of initial states and
# constants if these are passed in __call__.
if self._num_constants is not None:
    constants_shape = input_shape[-self._num_constants:]  # pylint: disable=E1130
else:
    constants_shape = None

if isinstance(input_shape, list):
    input_shape = input_shape[0]

batch_size = input_shape[0] if self.stateful else None
self.input_spec[0] = InputSpec(shape=(batch_size, None) + input_shape[2:5])

# allow cell (if layer) to build before we set or validate state_spec
if isinstance(self.cell, Layer):
    step_input_shape = (input_shape[0],) + input_shape[2:]
    if constants_shape is not None:
        self.cell.build([step_input_shape] + constants_shape)
    else:
        self.cell.build(step_input_shape)

    # set or validate state_spec
if hasattr(self.cell.state_size, '__len__'):
    state_size = list(self.cell.state_size)
else:
    state_size = [self.cell.state_size]

if self.state_spec is not None:
    # initial_state was passed in call, check compatibility
    if self.cell.data_format == 'channels_first':
        ch_dim = 1
    elif self.cell.data_format == 'channels_last':
        ch_dim = 3
    if [spec.shape[ch_dim] for spec in self.state_spec] != state_size:
        raise ValueError(
            'An initial_state was passed that is not compatible with '
            '`cell.state_size`. Received `state_spec`={}; '
            'However `cell.state_size` is '
            '{}'.format([spec.shape for spec in self.state_spec],
                        self.cell.state_size))
else:
    if self.cell.data_format == 'channels_first':
        self.state_spec = [InputSpec(shape=(None, dim, None, None))
                           for dim in state_size]
    elif self.cell.data_format == 'channels_last':
        self.state_spec = [InputSpec(shape=(None, None, None, dim))
                           for dim in state_size]
if self.stateful:
    self.reset_states()
self.built = True
