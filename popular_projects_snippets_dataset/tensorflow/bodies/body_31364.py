# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
config = config_pb2.ConfigProto()
config.allow_soft_placement = True

# Set up sequence lengths
np.random.seed([127])
sequence_length = max_time * np.ones((batch_size,))
inputs_list = [
    np.random.randn(batch_size, num_units).astype(np.float32)
    for _ in range(max_time)
]

# Halve the sequence length, full static unroll
with session.Session(config=config, graph=ops_lib.Graph()) as sess:
    with ops_lib.device("/cpu:0" if not use_gpu else None):
        inputs_list_t = [
            variables_lib.Variable(
                x, trainable=False).value() for x in inputs_list
        ]
        ops = _half_seq_len_vs_unroll_half_rnn_benchmark(inputs_list_t,
                                                         sequence_length / 2)
    variables_lib.global_variables_initializer().run()
    delta_half_seq_len = _timer(sess, ops)

# Halve the unroll size, don't use sequence length
with session.Session(config=config, graph=ops_lib.Graph()) as sess:
    with ops_lib.device("/cpu:0" if not use_gpu else None):
        inputs_list_t = [
            variables_lib.Variable(
                x, trainable=False).value() for x in inputs_list
        ]
        ops = _half_seq_len_vs_unroll_half_rnn_benchmark(
            inputs_list_t[:(max_time // 2)], sequence_length / 2)
    variables_lib.global_variables_initializer().run()
    delta_unroll_half = _timer(sess, ops)
print("%d \t %d \t\t %d \t %s \t %f \t\t %f \t\t %f" %
      (batch_size, max_time, num_units, use_gpu, delta_half_seq_len,
       delta_unroll_half, delta_half_seq_len / delta_unroll_half))

exit((delta_half_seq_len, delta_unroll_half))
