# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
config = config_pb2.ConfigProto()
config.allow_soft_placement = True

# Set up sequence lengths
np.random.seed([127])
sequence_length = np.random.randint(0, max_time, size=batch_size)
inputs_list = [
    np.random.randn(batch_size, num_units).astype(np.float32)
    for _ in range(max_time)
]
inputs = np.dstack(inputs_list).transpose([0, 2, 1])  # batch x time x depth

# Using rnn()
with session.Session(config=config, graph=ops_lib.Graph()) as sess:
    with ops_lib.device("/cpu:0" if not use_gpu else None):
        inputs_list_t = [
            variables_lib.Variable(
                x, trainable=False).value() for x in inputs_list
        ]
        ops = _static_vs_dynamic_rnn_benchmark_static(inputs_list_t,
                                                      sequence_length)
    variables_lib.global_variables_initializer().run()
    delta_static = _timer(sess, ops)

# Using dynamic_rnn()
with session.Session(config=config, graph=ops_lib.Graph()) as sess:
    with ops_lib.device("/cpu:0" if not use_gpu else None):
        inputs_t = variables_lib.Variable(inputs, trainable=False).value()
        ops = _static_vs_dynamic_rnn_benchmark_dynamic(inputs_t, sequence_length)
    variables_lib.global_variables_initializer().run()
    delta_dynamic = _timer(sess, ops)

print("%d \t %d \t %d \t %s \t %f \t %f \t %f" %
      (batch_size, max_time, num_units, use_gpu, delta_static, delta_dynamic,
       delta_dynamic / delta_static))

exit((delta_static, delta_dynamic))
