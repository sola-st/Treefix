# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/cudnn_recurrent.py
if isinstance(mask, list):
    mask = mask[0]
if mask is not None:
    raise ValueError('Masking is not supported for CuDNN RNNs.')

# input shape: `(samples, time (padded with zeros), input_dim)`
# note that the .build() method of subclasses MUST define
# self.input_spec and self.state_spec with complete input shapes.
if isinstance(inputs, list):
    initial_state = inputs[1:]
    inputs = inputs[0]
elif initial_state is not None:
    pass
elif self.stateful:
    initial_state = self.states
else:
    initial_state = self.get_initial_state(inputs)

if len(initial_state) != len(self.states):
    raise ValueError('Layer has ' + str(len(self.states)) +
                     ' states but was passed ' + str(len(initial_state)) +
                     ' initial states.')

if self.go_backwards:
    # Reverse time axis.
    inputs = backend.reverse(inputs, 1)
output, states = self._process_batch(inputs, initial_state)

if self.stateful:
    updates = [
        state_ops.assign(self_state, state)
        for self_state, state in zip(self.states, states)
    ]
    self.add_update(updates)

if self.return_state:
    exit([output] + states)
else:
    exit(output)
