# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
num_units = 3
input_size = 5
batch_size = 2
max_length = 8

initializer = init_ops.random_uniform_initializer(
    -0.01, 0.01, seed=self._seed)
sequence_length = array_ops.placeholder(
    dtypes.int64) if use_sequence_length else None
cell_fw = rnn_cell.LSTMCell(
    num_units, input_size, initializer=initializer, state_is_tuple=False)
cell_bw = rnn_cell.LSTMCell(
    num_units, input_size, initializer=initializer, state_is_tuple=False)
inputs = max_length * [
    array_ops.placeholder(
        dtypes.float32,
        shape=(batch_size, input_size) if use_shape else (None, input_size))
]
outputs, state_fw, state_bw = rnn.static_bidirectional_rnn(
    cell_fw,
    cell_bw,
    inputs,
    dtype=dtypes.float32,
    sequence_length=sequence_length,
    scope=scope)
self.assertEqual(len(outputs), len(inputs))
for out in outputs:
    self.assertEqual(out.get_shape().as_list(),
                     [batch_size if use_shape else None, 2 * num_units])

input_value = np.random.randn(batch_size, input_size)
outputs = array_ops.stack(outputs)

exit((input_value, inputs, outputs, state_fw, state_bw, sequence_length))
