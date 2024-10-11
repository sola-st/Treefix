# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
cell = Plus1RNNCell()
batch_size = 2
input_size = 5
max_length = 8  # unrolled up to this length
inputs = max_length * [
    array_ops.placeholder(dtypes.float32, shape=(batch_size, input_size))
]
exit(rnn.static_rnn(cell, inputs, dtype=dtypes.float32, scope=scope))
