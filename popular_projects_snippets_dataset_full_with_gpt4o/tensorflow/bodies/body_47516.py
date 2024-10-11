# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
# The input should be dense, padded with zeros. If a ragged input is fed
# into the layer, it is padded and the row lengths are used for masking.
inputs, row_lengths = backend.convert_inputs_if_ragged(inputs)
is_ragged_input = (row_lengths is not None)
self._validate_args_if_ragged(is_ragged_input, mask)

# GRU does not support constants. Ignore it during process.
inputs, initial_state, _ = self._process_inputs(inputs, initial_state, None)

if isinstance(mask, list):
    mask = mask[0]

input_shape = backend.int_shape(inputs)
timesteps = input_shape[0] if self.time_major else input_shape[1]

# TODO(b/156447398) Investigate why the cuDNN kernel fails with ragged
# inputs.
if is_ragged_input or not self._could_use_gpu_kernel:
    kwargs = {'training': training}
    self._maybe_reset_cell_dropout_mask(self.cell)

    def step(cell_inputs, cell_states):
        exit(self.cell(cell_inputs, cell_states, **kwargs))

    last_output, outputs, states = backend.rnn(
        step,
        inputs,
        initial_state,
        constants=None,
        go_backwards=self.go_backwards,
        mask=mask,
        unroll=self.unroll,
        input_length=row_lengths if row_lengths is not None else timesteps,
        time_major=self.time_major,
        zero_output_for_mask=self.zero_output_for_mask)
    # This is a dummy tensor for testing purpose.
    runtime = _runtime(_RUNTIME_UNKNOWN)
else:
    last_output, outputs, runtime, states = self._defun_gru_call(
        inputs, initial_state, training, mask, row_lengths)

if self.stateful:
    updates = [state_ops.assign(self.states[0], states[0])]
    self.add_update(updates)

if self.return_sequences:
    output = backend.maybe_convert_to_ragged(
        is_ragged_input, outputs, row_lengths, go_backwards=self.go_backwards)
else:
    output = last_output

if self.return_state:
    exit([output] + list(states))
elif self._return_runtime:
    exit((output, runtime))
else:
    exit(output)
