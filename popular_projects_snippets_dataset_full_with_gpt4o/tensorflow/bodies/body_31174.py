# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
cell = Plus1RNNCell()
inputs = [array_ops.placeholder(dtypes.float32, shape=(3, 4))]
with self.assertRaisesRegex(ValueError, "must be a vector"):
    rnn.static_rnn(cell, inputs, dtype=dtypes.float32, sequence_length=4)
