# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
# Use the new defun approach for backend implementation swap.
# Note that different implementations need to have same function
# signature, eg, the tensor parameters need to have same shape and dtypes.

self.reset_dropout_mask()
dropout_mask = self.get_dropout_mask_for_cell(inputs, training, count=3)
if dropout_mask is not None:
    inputs = inputs * dropout_mask[0]

if _use_new_code():
    gru_kwargs = {
        'inputs': inputs,
        'init_h': _read_variable_value(initial_state[0]),
        'kernel': _read_variable_value(self.cell.kernel),
        'recurrent_kernel': _read_variable_value(self.cell.recurrent_kernel),
        'bias': _read_variable_value(self.cell.bias),
        'mask': mask,
        'time_major': self.time_major,
        'go_backwards': self.go_backwards,
        'sequence_lengths': sequence_lengths,
        'zero_output_for_mask': self.zero_output_for_mask
    }
    (last_output, outputs, new_h,
     runtime) = self._defun_wrapper.defun_layer(**gru_kwargs)
else:
    gpu_gru_kwargs = {
        'inputs': inputs,
        'init_h': _read_variable_value(initial_state[0]),
        'kernel': _read_variable_value(self.cell.kernel),
        'recurrent_kernel': _read_variable_value(self.cell.recurrent_kernel),
        'bias': _read_variable_value(self.cell.bias),
        'mask': mask,
        'time_major': self.time_major,
        'go_backwards': self.go_backwards,
        'sequence_lengths': sequence_lengths
    }
    normal_gru_kwargs = gpu_gru_kwargs.copy()
    normal_gru_kwargs.update({
        'zero_output_for_mask': self.zero_output_for_mask,
    })

    if context.executing_eagerly():
        device_type = _get_context_device_type()
        can_use_gpu = (
            # Either user specified GPU or unspecified but GPU is available.
            (device_type == _GPU_DEVICE_NAME or
             (device_type is None and config.list_logical_devices('GPU'))) and
            (mask is None or is_cudnn_supported_inputs(mask, self.time_major)))
        # Under eager context, check the device placement and prefer the
        if can_use_gpu:
            last_output, outputs, new_h, runtime = gpu_gru(**gpu_gru_kwargs)
        else:
            last_output, outputs, new_h, runtime = standard_gru(
                **normal_gru_kwargs)
    else:
        last_output, outputs, new_h, runtime = gru_with_backend_selection(
            **normal_gru_kwargs)

states = [new_h]
exit((last_output, outputs, runtime, states))
