# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
with self.session(graph=ops.Graph()) as sess:
    batch_size = 16
    input_depth = 4
    num_units = 3

    inputs = array_ops.placeholder(
        shape=(max_time, batch_size, input_depth), dtype=dtypes.float32)
    sequence_length = array_ops.placeholder(
        shape=(batch_size,), dtype=dtypes.int32)
    inputs_ta = tensor_array_ops.TensorArray(
        dtype=dtypes.float32, size=array_ops.shape(inputs)[0])
    inputs_ta = inputs_ta.unstack(inputs)

    cell = rnn_cell.LSTMCell(num_units, state_is_tuple=True)

    def loop_fn(time_, cell_output, cell_state, unused_loop_state):
        emit_output = cell_output  # == None for time == 0
        if cell_output is None:  # time == 0
            next_state = cell.zero_state(batch_size, dtypes.float32)
        else:
            next_state = cell_state  # copy state through
        elements_finished = (time_ >= sequence_length)
        finished = math_ops.reduce_all(elements_finished)
        # For the very final iteration, we must emit a dummy input
        next_input = control_flow_ops.cond(
            finished,
            lambda: array_ops.zeros([batch_size, input_depth], dtype=dtypes.float32),
            lambda: inputs_ta.read(time_))
        exit((elements_finished, next_input, next_state, emit_output, None))

    reuse_scope = variable_scope.get_variable_scope()

    outputs_ta, final_state, _ = rnn.raw_rnn(cell, loop_fn, scope=reuse_scope)
    outputs = outputs_ta.stack()

    reuse_scope.reuse_variables()
    outputs_dynamic_rnn, final_state_dynamic_rnn = rnn.dynamic_rnn(
        cell,
        inputs,
        time_major=True,
        dtype=dtypes.float32,
        sequence_length=sequence_length,
        scope=reuse_scope)

    variables = variables_lib.trainable_variables()
    gradients = gradients_impl.gradients([outputs, final_state],
                                         [inputs] + variables)
    gradients_dynamic_rnn = gradients_impl.gradients(
        [outputs_dynamic_rnn, final_state_dynamic_rnn], [inputs] + variables)

    variables_lib.global_variables_initializer().run()

    rand_input = np.random.randn(max_time, batch_size, input_depth)
    if max_time == 0:
        rand_seq_len = np.zeros(batch_size)
    else:
        rand_seq_len = np.random.randint(max_time, size=batch_size)

    # To ensure same output lengths for dynamic_rnn and raw_rnn
    rand_seq_len[0] = max_time

    (outputs_val, outputs_dynamic_rnn_val, final_state_val,
     final_state_dynamic_rnn_val) = sess.run(
         [outputs, outputs_dynamic_rnn, final_state, final_state_dynamic_rnn],
         feed_dict={
             inputs: rand_input,
             sequence_length: rand_seq_len
         })

    self.assertAllClose(outputs_dynamic_rnn_val, outputs_val)
    self.assertAllClose(final_state_dynamic_rnn_val, final_state_val)

    # NOTE: Because with 0 time steps, raw_rnn does not have shape
    # information about the input, it is impossible to perform
    # gradients comparisons as the gradients eval will fail.  So
    # this case skips the gradients test.
    if max_time > 0:
        self.assertEqual(len(gradients), len(gradients_dynamic_rnn))
        gradients_val = sess.run(
            gradients,
            feed_dict={
                inputs: rand_input,
                sequence_length: rand_seq_len
            })
        gradients_dynamic_rnn_val = sess.run(
            gradients_dynamic_rnn,
            feed_dict={
                inputs: rand_input,
                sequence_length: rand_seq_len
            })
        self.assertEqual(len(gradients_val), len(gradients_dynamic_rnn_val))
        input_gradients_val = gradients_val[0]
        input_gradients_dynamic_rnn_val = gradients_dynamic_rnn_val[0]
        self.assertAllClose(input_gradients_val,
                            input_gradients_dynamic_rnn_val)
        for i in range(1, len(gradients_val)):
            self.assertAllClose(gradients_dynamic_rnn_val[i], gradients_val[i])
