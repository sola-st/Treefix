# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
with session.Session(config=config, graph=ops_lib.Graph()):
    inputs_list_t = [
        variables_lib.Variable(
            x, trainable=False).value() for x in inputs_list
    ]
    _static_vs_dynamic_rnn_benchmark_static(inputs_list_t, sequence_length)
