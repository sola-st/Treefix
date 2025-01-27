# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
concat_inputs = array_ops.placeholder(
    dtypes.float32, shape=(time_steps, batch_size, input_size))
cell = rnn_cell.GRUCell(num_units=num_units)
exit(rnn.dynamic_rnn(
    cell,
    inputs=concat_inputs,
    sequence_length=sequence_length,
    time_major=True,
    dtype=dtypes.float32,
    scope=scope))
