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

# Run with concatenated states (default)
with session.Session(config=config, graph=ops_lib.Graph()) as sess:
    with ops_lib.device("/cpu:0" if not use_gpu else None):
        inputs_list_t = [
            variables_lib.Variable(
                x, trainable=False).value() for x in inputs_list
        ]
        ops = _concat_state_vs_tuple_state_rnn_benchmark(
            inputs_list_t, sequence_length, state_is_tuple=False)
    variables_lib.global_variables_initializer().run()
    delta_concat_state = _timer(sess, ops)

# Run with tuple states (new)
with session.Session(config=config, graph=ops_lib.Graph()) as sess:
    with ops_lib.device("/cpu:0" if not use_gpu else None):
        inputs_list_t = [
            variables_lib.Variable(
                x, trainable=False).value() for x in inputs_list
        ]
        ops = _concat_state_vs_tuple_state_rnn_benchmark(
            inputs_list_t, sequence_length, state_is_tuple=True)
    variables_lib.global_variables_initializer().run()
    delta_tuple_state = _timer(sess, ops)
print("%d \t %d \t %d \t %s \t %f \t\t %f \t\t %f" %
      (batch_size, max_time, num_units, use_gpu, delta_concat_state,
       delta_tuple_state, delta_concat_state / delta_tuple_state))

exit((delta_concat_state, delta_tuple_state))
