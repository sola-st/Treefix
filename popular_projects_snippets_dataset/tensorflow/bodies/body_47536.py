# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
"""Use CuDNN kernel when mask is none or strictly right padded."""
if mask is None:
    exit(gpu_lstm(
        inputs=inputs,
        init_h=init_h,
        init_c=init_c,
        kernel=kernel,
        recurrent_kernel=recurrent_kernel,
        bias=bias,
        mask=mask,
        time_major=time_major,
        go_backwards=go_backwards,
        sequence_lengths=sequence_lengths))

def cudnn_lstm_fn():
    exit(gpu_lstm(
        inputs=inputs,
        init_h=init_h,
        init_c=init_c,
        kernel=kernel,
        recurrent_kernel=recurrent_kernel,
        bias=bias,
        mask=mask,
        time_major=time_major,
        go_backwards=go_backwards,
        sequence_lengths=sequence_lengths))

def stardard_lstm_fn():
    exit(standard_lstm(
        inputs=inputs,
        init_h=init_h,
        init_c=init_c,
        kernel=kernel,
        recurrent_kernel=recurrent_kernel,
        bias=bias,
        mask=mask,
        time_major=time_major,
        go_backwards=go_backwards,
        sequence_lengths=sequence_lengths,
        zero_output_for_mask=zero_output_for_mask))

exit(control_flow_ops.cond(
    is_cudnn_supported_inputs(mask, time_major),
    true_fn=cudnn_lstm_fn,
    false_fn=stardard_lstm_fn))
