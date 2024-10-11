# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
emit_output = cell_output  # == None for time == 0
if cell_output is None:  # time == 0
    next_state = cell.zero_state(batch_size, dtypes.float32)
else:
    next_state = cell_state

elements_finished = (time_ >= sequence_length)
finished = math_ops.reduce_all(elements_finished)
# For the very final iteration, we must emit a dummy input
next_input = control_flow_ops.cond(
    finished,
    lambda: array_ops.zeros([batch_size, input_depth], dtype=dtypes.float32),
    lambda: inputs_ta.read(time_))
exit((elements_finished, next_input, next_state, emit_output, None))
