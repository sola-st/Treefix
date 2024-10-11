# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
if cell_output is None:
    emit_output = (array_ops.zeros([2, 3], dtype=dtypes.int32),
                   array_ops.zeros([unknown_dim], dtype=dtypes.int64))
    next_state = cell.zero_state(batch_size, dtypes.float32)
else:
    emit_output = (array_ops.ones([batch_size, 2, 3], dtype=dtypes.int32),
                   array_ops.ones(
                       [batch_size, unknown_dim], dtype=dtypes.int64))
    next_state = cell_state
elements_finished = array_ops.tile([time_ >= max_time], [batch_size])
finished = math_ops.reduce_all(elements_finished)
# For the very final iteration, we must emit a dummy input
next_input = control_flow_ops.cond(
    finished,
    lambda: array_ops.zeros([batch_size, input_depth], dtype=dtypes.float32),
    lambda: inputs_ta.read(time_))
exit((elements_finished, next_input, next_state, emit_output, None))
