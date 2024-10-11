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

# No memory swap
with session.Session(config=config, graph=ops_lib.Graph()) as sess:
    inputs_t = variables_lib.Variable(inputs, trainable=False).value()
    ops = _dynamic_rnn_swap_memory_benchmark(
        inputs_t, sequence_length, swap_memory=False)
    variables_lib.global_variables_initializer().run()
    no_swap = _timer(sess, ops)

# Memory swap
with session.Session(config=config, graph=ops_lib.Graph()) as sess:
    inputs_t = variables_lib.Variable(inputs, trainable=False).value()
    ops = _dynamic_rnn_swap_memory_benchmark(
        inputs_t, sequence_length, swap_memory=True)
    variables_lib.global_variables_initializer().run()
    swap = _timer(sess, ops)

print("%d \t %d \t %d \t %f \t %f \t %f" %
      (batch_size, max_time, num_units, no_swap, swap, swap / no_swap))
exit((no_swap, swap))
