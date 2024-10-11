# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent.py
# The input should be dense, padded with zeros. If a ragged input is fed
# into the layer, it is padded and the row lengths are used for masking.
inputs, row_lengths = backend.convert_inputs_if_ragged(inputs)
is_ragged_input = (row_lengths is not None)
self._validate_args_if_ragged(is_ragged_input, mask)

inputs, initial_state, constants = self._process_inputs(
    inputs, initial_state, constants)

self._maybe_reset_cell_dropout_mask(self.cell)
if isinstance(self.cell, StackedRNNCells):
    for cell in self.cell.cells:
        self._maybe_reset_cell_dropout_mask(cell)

if mask is not None:
    # Time step masks must be the same for each input.
    # TODO(scottzhu): Should we accept multiple different masks?
    mask = nest.flatten(mask)[0]

if nest.is_nested(inputs):
    # In the case of nested input, use the first element for shape check.
    input_shape = backend.int_shape(nest.flatten(inputs)[0])
else:
    input_shape = backend.int_shape(inputs)
timesteps = input_shape[0] if self.time_major else input_shape[1]
if self.unroll and timesteps is None:
    raise ValueError('Cannot unroll a RNN if the '
                     'time dimension is undefined. \n'
                     '- If using a Sequential model, '
                     'specify the time dimension by passing '
                     'an `input_shape` or `batch_input_shape` '
                     'argument to your first layer. If your '
                     'first layer is an Embedding, you can '
                     'also use the `input_length` argument.\n'
                     '- If using the functional API, specify '
                     'the time dimension by passing a `shape` '
                     'or `batch_shape` argument to your Input layer.')

kwargs = {}
if generic_utils.has_arg(self.cell.call, 'training'):
    kwargs['training'] = training

# TF RNN cells expect single tensor as state instead of list wrapped tensor.
is_tf_rnn_cell = getattr(self.cell, '_is_tf_rnn_cell', None) is not None
# Use the __call__ function for callable objects, eg layers, so that it
# will have the proper name scopes for the ops, etc.
cell_call_fn = self.cell.__call__ if callable(self.cell) else self.cell.call
if constants:
    if not generic_utils.has_arg(self.cell.call, 'constants'):
        raise ValueError('RNN cell does not support constants')

    def step(inputs, states):
        constants = states[-self._num_constants:]  # pylint: disable=invalid-unary-operand-type
        states = states[:-self._num_constants]  # pylint: disable=invalid-unary-operand-type

        states = states[0] if len(states) == 1 and is_tf_rnn_cell else states
        output, new_states = cell_call_fn(
            inputs, states, constants=constants, **kwargs)
        if not nest.is_nested(new_states):
            new_states = [new_states]
        exit((output, new_states))
else:

    def step(inputs, states):
        states = states[0] if len(states) == 1 and is_tf_rnn_cell else states
        output, new_states = cell_call_fn(inputs, states, **kwargs)
        if not nest.is_nested(new_states):
            new_states = [new_states]
        exit((output, new_states))
last_output, outputs, states = backend.rnn(
    step,
    inputs,
    initial_state,
    constants=constants,
    go_backwards=self.go_backwards,
    mask=mask,
    unroll=self.unroll,
    input_length=row_lengths if row_lengths is not None else timesteps,
    time_major=self.time_major,
    zero_output_for_mask=self.zero_output_for_mask)

if self.stateful:
    updates = [
        state_ops.assign(self_state, state) for self_state, state in zip(
            nest.flatten(self.states), nest.flatten(states))
    ]
    self.add_update(updates)

if self.return_sequences:
    output = backend.maybe_convert_to_ragged(
        is_ragged_input, outputs, row_lengths, go_backwards=self.go_backwards)
else:
    output = last_output

if self.return_state:
    if not isinstance(states, (list, tuple)):
        states = [states]
    else:
        states = list(states)
    exit(generic_utils.to_list(output) + states)
else:
    exit(output)
