# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
with context.eager_mode():
    cell = TensorArrayStateRNNCell()
    inputs = np.array([[[1], [2], [3], [4]]], dtype=np.float32)
    rnn.dynamic_rnn(cell, inputs, dtype=dtypes.float32, sequence_length=[4])
