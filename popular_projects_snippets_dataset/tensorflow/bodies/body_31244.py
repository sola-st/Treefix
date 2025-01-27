# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
if cell_output is None:
    loop_state = tensor_array_ops.TensorArray(
        dynamic_size=True,
        size=0,
        dtype=dtypes.int32,
        clear_after_read=False)
    loop_state = loop_state.write(0, 1)
    next_state = cell.zero_state(batch_size, dtypes.float32)
else:
    loop_state = loop_state.write(time_,
                                  loop_state.read(time_ - 1) + time_)
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
