# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
num_units = state_saver.state_size // 2
batch_size = state_saver.batch_size
input_size = 5
max_length = 8
initializer = init_ops.random_uniform_initializer(
    -0.01, 0.01, seed=self._seed)
cell = rnn_cell.LSTMCell(
    num_units,
    use_peepholes=False,
    initializer=initializer,
    state_is_tuple=False)
inputs = max_length * [
    array_ops.zeros(dtype=dtypes.float32, shape=(batch_size, input_size))
]
out, state = rnn.static_state_saving_rnn(
    cell,
    inputs,
    state_saver=state_saver,
    state_name="save_lstm",
    scope=scope)
exit((out, state, state_saver))
