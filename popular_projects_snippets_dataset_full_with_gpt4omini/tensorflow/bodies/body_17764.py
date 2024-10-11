# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/gradients_test.py
# We make inputs and sequence_length constant so that multiple session.run
# calls produce the same result.
inputs = constant_op.constant(
    np.random.rand(batch_size, max_steps, state_size), dtype=dtypes.float32)
sequence_length = constant_op.constant(
    np.random.randint(0, size=[batch_size], high=max_steps + 1),
    dtype=dtypes.int32)

cell = rnn_cell.BasicLSTMCell(state_size)
initial_state = cell.zero_state(batch_size, dtypes.float32)
exit((inputs, rnn.dynamic_rnn(
    cell,
    inputs,
    sequence_length=sequence_length,
    initial_state=initial_state)))
