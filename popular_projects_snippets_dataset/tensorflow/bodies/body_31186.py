# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
num_units = 3
input_size = 5
batch_size = 2
max_length = 8
with self.session(graph=ops.Graph()) as sess:
    initializer = init_ops.random_uniform_initializer(
        -0.01, 0.01, seed=self._seed)
    state_saver = TestStateSaver(batch_size, num_units)
    cell = rnn_cell.LSTMCell(
        num_units,
        use_peepholes=False,
        initializer=initializer,
        state_is_tuple=True)
    inputs = max_length * [
        array_ops.placeholder(dtypes.float32, shape=(batch_size, input_size))
    ]
    with variable_scope.variable_scope("share_scope"):
        outputs, state = rnn.static_state_saving_rnn(
            cell, inputs, state_saver=state_saver, state_name=("c", "m"))
    self.assertEqual(len(outputs), len(inputs))
    for out in outputs:
        self.assertEqual(out.get_shape().as_list(), [batch_size, num_units])

    variables_lib.global_variables_initializer().run()
    input_value = np.random.randn(batch_size, input_size)
    last_and_saved_states = sess.run(
        state + (state_saver.saved_state["c"], state_saver.saved_state["m"]),
        feed_dict={
            inputs[0]: input_value
        })
    self.assertEqual(4, len(last_and_saved_states))
    self.assertAllEqual(last_and_saved_states[:2], last_and_saved_states[2:])
