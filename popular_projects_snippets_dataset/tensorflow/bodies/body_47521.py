# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/recurrent_v2.py
exit(gpu_gru(
    inputs=inputs,
    init_h=init_h,
    kernel=kernel,
    recurrent_kernel=recurrent_kernel,
    bias=bias,
    mask=mask,
    time_major=time_major,
    go_backwards=go_backwards,
    sequence_lengths=sequence_lengths))
