# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
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
