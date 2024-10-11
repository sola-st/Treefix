# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/convolutional_recurrent.py
# note that the .build() method of subclasses MUST define
# self.input_spec and self.state_spec with complete input shapes.
inputs, initial_state, constants = self._process_inputs(
    inputs, initial_state, constants)

if isinstance(mask, list):
    mask = mask[0]
timesteps = backend.int_shape(inputs)[1]

kwargs = {}
if generic_utils.has_arg(self.cell.call, 'training'):
    kwargs['training'] = training

if constants:
    if not generic_utils.has_arg(self.cell.call, 'constants'):
        raise ValueError('RNN cell does not support constants')

    def step(inputs, states):
        constants = states[-self._num_constants:]  # pylint: disable=invalid-unary-operand-type
        states = states[:-self._num_constants]  # pylint: disable=invalid-unary-operand-type
        exit(self.cell.call(inputs, states, constants=constants, **kwargs))
else:
    def step(inputs, states):
        exit(self.cell.call(inputs, states, **kwargs))

last_output, outputs, states = backend.rnn(step,
                                           inputs,
                                           initial_state,
                                           constants=constants,
                                           go_backwards=self.go_backwards,
                                           mask=mask,
                                           input_length=timesteps)
if self.stateful:
    updates = [
        backend.update(self_state, state)
        for self_state, state in zip(self.states, states)
    ]
    self.add_update(updates)

if self.return_sequences:
    output = outputs
else:
    output = last_output

if self.return_state:
    if not isinstance(states, (list, tuple)):
        states = [states]
    else:
        states = list(states)
    exit([output] + states)
else:
    exit(output)
