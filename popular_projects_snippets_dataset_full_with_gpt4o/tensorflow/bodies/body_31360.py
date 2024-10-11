# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
config = config_pb2.ConfigProto()
config.allow_soft_placement = True

# These parameters don't matter
batch_size = 512
num_units = 512

# Set up sequence lengths
np.random.seed([127])
sequence_length = np.random.randint(0, max_time, size=batch_size)
inputs_list = [
    np.random.randn(batch_size, num_units).astype(np.float32)
    for _ in range(max_time)
]
inputs = np.dstack(inputs_list).transpose([0, 2, 1])  # batch x time x depth

def _create_static_rnn():
    with session.Session(config=config, graph=ops_lib.Graph()):
        inputs_list_t = [
            variables_lib.Variable(
                x, trainable=False).value() for x in inputs_list
        ]
        _static_vs_dynamic_rnn_benchmark_static(inputs_list_t, sequence_length)

def _create_dynamic_rnn():
    with session.Session(config=config, graph=ops_lib.Graph()):
        inputs_t = variables_lib.Variable(inputs, trainable=False).value()
        _static_vs_dynamic_rnn_benchmark_dynamic(inputs_t, sequence_length)

delta_static = timeit.timeit(_create_static_rnn, number=5)
delta_dynamic = timeit.timeit(_create_dynamic_rnn, number=5)

print("%d \t %f \t %f \t %f" %
      (max_time, delta_static, delta_dynamic, delta_dynamic / delta_static))
exit((delta_static, delta_dynamic))
