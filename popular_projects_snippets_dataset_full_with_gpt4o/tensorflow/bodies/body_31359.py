# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
with session.Session(config=config, graph=ops_lib.Graph()):
    inputs_t = variables_lib.Variable(inputs, trainable=False).value()
    _static_vs_dynamic_rnn_benchmark_dynamic(inputs_t, sequence_length)
