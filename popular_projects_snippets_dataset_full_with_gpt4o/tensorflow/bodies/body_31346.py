# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_test.py
if context.executing_eagerly():
    inputs = np.zeros((3, 4, 5), dtype=np.int32)
else:
    inputs = array_ops.placeholder(dtypes.int32, shape=(3, 4, 5))

cells = [
    rnn_cell_impl.BasicRNNCell,
    rnn_cell_impl.GRUCell,
    rnn_cell_impl.BasicLSTMCell,
    rnn_cell_impl.LSTMCell,
]
for cell_cls in cells:
    with self.cached_session():
        with self.assertRaisesRegex(ValueError,
                                    "RNN cell only supports floating"):
            cell = cell_cls(2, dtype=dtypes.int32)
            rnn.dynamic_rnn(cell, inputs, dtype=dtypes.int32)
