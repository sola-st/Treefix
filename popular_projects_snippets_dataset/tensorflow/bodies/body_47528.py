# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
# The input should be dense, padded with zeros. If a ragged input is fed
# into the layer, it is padded and the row lengths are used for masking.
inputs, row_lengths = backend.convert_inputs_if_ragged(inputs)
is_ragged_input = (row_lengths is not None)
self._validate_args_if_ragged(is_ragged_input, mask)

# LSTM does not support constants. Ignore it during process.
inputs, initial_state, _ = self._process_inputs(inputs, initial_state, None)

if isinstance(mask, list):
    mask = mask[0]

input_shape = backend.int_shape(inputs)
timesteps = input_shape[0] if self.time_major else input_shape[1]

# TODO(b/156447398) Investigate why the cuDNN kernel fails with ragged
# inputs.
if is_ragged_input or not self._could_use_gpu_kernel:
    # Fall back to use the normal LSTM.
    kwargs = {'training': training}
    self._maybe_reset_cell_dropout_mask(self.cell)

    def step(inputs, states):
        exit(self.cell(inputs, states, **kwargs))

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
    runtime = _runtime(_RUNTIME_UNKNOWN)
else:
    # Use the new defun approach for backend implementation swap.
    # Note that different implementations need to have same function
    # signature, eg, the tensor parameters need to have same shape and dtypes.
    # Since the CuDNN has an extra set of bias, those bias will be passed to
    # both normal and CuDNN implementations.
    self.reset_dropout_mask()
    dropout_mask = self.get_dropout_mask_for_cell(inputs, training, count=4)
    if dropout_mask is not None:
        inputs = inputs * dropout_mask[0]
    if _use_new_code():
        lstm_kwargs = {
            'inputs':
                inputs,
            'init_h':
                _read_variable_value(initial_state[0]),
            'init_c':
                _read_variable_value(initial_state[1]),
            'kernel':
                _read_variable_value(self.cell.kernel),
            'recurrent_kernel':
                _read_variable_value(self.cell.recurrent_kernel),
            'bias':
                _read_variable_value(self.cell.bias),
            'mask':
                mask,
            'time_major':
                self.time_major,
            'go_backwards':
                self.go_backwards,
            'sequence_lengths':
                row_lengths,
            'zero_output_for_mask':
                self.zero_output_for_mask,
        }
        (last_output, outputs, new_h, new_c,
         runtime) = self._defun_wrapper.defun_layer(**lstm_kwargs)
    else:
        gpu_lstm_kwargs = {
            'inputs':
                inputs,
            'init_h':
                _read_variable_value(initial_state[0]),
            'init_c':
                _read_variable_value(initial_state[1]),
            'kernel':
                _read_variable_value(self.cell.kernel),
            'recurrent_kernel':
                _read_variable_value(self.cell.recurrent_kernel),
            'bias':
                _read_variable_value(self.cell.bias),
            'mask':
                mask,
            'time_major':
                self.time_major,
            'go_backwards':
                self.go_backwards,
            'sequence_lengths':
                row_lengths
        }
        normal_lstm_kwargs = gpu_lstm_kwargs.copy()
        normal_lstm_kwargs.update({
            'zero_output_for_mask': self.zero_output_for_mask,
        })

        if context.executing_eagerly():
            device_type = _get_context_device_type()
            can_use_gpu = (
                # Either user specified GPU or unspecified but GPU is available.
                (device_type == _GPU_DEVICE_NAME or
                 (device_type is None and config.list_logical_devices('GPU'))) and
                (mask is None or
                 is_cudnn_supported_inputs(mask, self.time_major)))
            # Under eager context, check the device placement and prefer the
            # GPU implementation when GPU is available.
            if can_use_gpu:
                last_output, outputs, new_h, new_c, runtime = gpu_lstm(
                    **gpu_lstm_kwargs)
            else:
                last_output, outputs, new_h, new_c, runtime = standard_lstm(
                    **normal_lstm_kwargs)
        else:
            (last_output, outputs, new_h, new_c,
             runtime) = lstm_with_backend_selection(**normal_lstm_kwargs)

    states = [new_h, new_c]

if self.stateful:
    updates = [
        state_ops.assign(self_state, state)
        for self_state, state in zip(self.states, states)
    ]
    self.add_update(updates)

if self.return_sequences:
    output = backend.maybe_convert_to_ragged(
        is_ragged_input, outputs, row_lengths, go_backwards=self.go_backwards)
else:
    output = last_output

if self.return_state:
    exit([output] + list(states))
elif self.return_runtime:
    exit((output, runtime))
else:
    exit(output)
