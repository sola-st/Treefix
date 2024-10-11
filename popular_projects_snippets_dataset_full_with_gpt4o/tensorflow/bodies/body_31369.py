# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
config = config_pb2.ConfigProto()
config.allow_soft_placement = True

# Set up sequence lengths
np.random.seed([127])
sequence_length = [seqlen for _ in range(batch_size)]
inputs_list = [
    np.random.randn(batch_size, num_units).astype(np.float32)
    for _ in range(seqlen)
]
inputs = np.dstack(inputs_list).transpose([0, 2, 1])  # batch x time x depth

for _ in range(nn):
    if dynamic:
        with session.Session(config=config, graph=ops_lib.Graph()) as sess:
            inputs_t = variables_lib.Variable(inputs, trainable=False).value()
            ops = _dynamic_rnn_swap_memory_benchmark(
                inputs_t, sequence_length, swap_memory=swap_memory)
            variables_lib.global_variables_initializer().run()
            elapsed = _timer(sess, ops)
    else:
        with session.Session(config=config, graph=ops_lib.Graph()) as sess:
            inputs_list_t = [
                variables_lib.Variable(
                    x, trainable=False).value() for x in inputs_list
            ]
            ops = _static_vs_dynamic_rnn_benchmark_static(inputs_list_t,
                                                          sequence_length)
            variables_lib.global_variables_initializer().run()
            elapsed = _timer(sess, ops)

    print("%d \t %d \t %d \t %s \t %f \t %f" % (batch_size, seqlen, num_units,
                                                dynamic, elapsed,
                                                elapsed / seqlen))
