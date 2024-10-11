# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
if cell_output is None:
    loop_state = constant_op.constant([0])
    next_state = cell.zero_state(batch_size, dtypes.float32)
else:
    loop_state = array_ops.stack([array_ops.squeeze(loop_state) + 1])
    next_state = cell_state
emit_output = cell_output  # == None for time == 0
elements_finished = array_ops.tile([time_ >= max_time], [batch_size])
finished = math_ops.reduce_all(elements_finished)
# For the very final iteration, we must emit a dummy input
next_input = control_flow_ops.cond(
    finished,
    lambda: array_ops.zeros([batch_size, input_depth], dtype=dtypes.float32),
    lambda: inputs_ta.read(time_))
exit((elements_finished, next_input, next_state, emit_output,
        loop_state))
