# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
num_units = 3
input_size = 5
batch_size = 2
max_length = 8

initializer = init_ops.random_uniform_initializer(
    -0.01, 0.01, seed=self._seed)
sequence_length = (
    array_ops.placeholder(dtypes.int64) if use_sequence_length else None)
cell_fw = rnn_cell.LSTMCell(
    num_units, initializer=initializer, state_is_tuple=use_state_tuple)
cell_bw = rnn_cell.LSTMCell(
    num_units, initializer=initializer, state_is_tuple=use_state_tuple)
inputs = max_length * [
    array_ops.placeholder(
        dtypes.float32,
        shape=(batch_size if use_shape else None, input_size))
]
inputs_c = array_ops.stack(inputs)
if not use_time_major:
    inputs_c = array_ops.transpose(inputs_c, [1, 0, 2])
outputs, states = rnn.bidirectional_dynamic_rnn(
    cell_fw,
    cell_bw,
    inputs_c,
    sequence_length,
    dtype=dtypes.float32,
    time_major=use_time_major,
    scope=scope)
outputs = array_ops.concat(outputs, 2)
state_fw, state_bw = states
outputs_shape = [None, max_length, 2 * num_units]
if use_shape:
    outputs_shape[0] = batch_size
if use_time_major:
    outputs_shape[0], outputs_shape[1] = outputs_shape[1], outputs_shape[0]
self.assertEqual(outputs.get_shape().as_list(), outputs_shape)

input_value = np.random.randn(batch_size, input_size)

exit((input_value, inputs, outputs, state_fw, state_bw, sequence_length))
