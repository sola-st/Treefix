# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
with self.session(graph=ops.Graph()) as sess:
    max_time = 10
    batch_size = 16
    input_depth = 4
    num_units = 3

    inputs = np.random.randn(max_time, batch_size, input_depth)
    inputs_ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32, size=array_ops.shape(inputs)[0])
    inputs_ta = inputs_ta.unstack(inputs)
    # Verify emit shapes may be unknown by feeding a placeholder that
    # determines an emit shape.
    unknown_dim = array_ops.placeholder(dtype=dtypes.int32)

    cell = rnn_cell.LSTMCell(num_units, state_is_tuple=True)

    def loop_fn(time_, cell_output, cell_state, _):
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

    r = rnn.raw_rnn(cell, loop_fn)
    output_ta = r[0]
    self.assertEqual(2, len(output_ta))
    self.assertEqual([dtypes.int32, dtypes.int64],
                     [ta.dtype for ta in output_ta])
    output = [ta.stack() for ta in output_ta]
    output_vals = sess.run(output, feed_dict={unknown_dim: 1})
    self.assertAllEqual(
        np.ones((max_time, batch_size, 2, 3), np.int32), output_vals[0])
    self.assertAllEqual(
        np.ones((max_time, batch_size, 1), np.int64), output_vals[1])
