# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
with self.session(graph=ops.Graph()):
    max_time = 10
    batch_size = 16
    input_depth = 4
    num_units = 3

    inputs = np.random.randn(max_time, batch_size, input_depth)
    inputs_ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32, size=array_ops.shape(inputs)[0])
    inputs_ta = inputs_ta.unstack(inputs)

    cell = rnn_cell.LSTMCell(num_units, state_is_tuple=True)

    def loop_fn(time_, cell_output, cell_state, loop_state):
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

    r = rnn.raw_rnn(cell, loop_fn)
    loop_state = r[-1]
    self.assertEqual([10], self.evaluate(loop_state))
