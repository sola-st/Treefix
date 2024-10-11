# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
num_units = 3
input_size = 5
batch_size = 2
max_length = 8
with self.session(graph=ops.Graph()) as sess:
    initializer = init_ops.random_uniform_initializer(
        -0.01, 0.01, seed=self._seed)
    state_saver = TestStateSaver(
        batch_size, {
            "c0": num_units,
            "m0": num_units,
            "c1": num_units + 1,
            "m1": num_units + 1,
            "c2": num_units + 2,
            "m2": num_units + 2,
            "c3": num_units + 3,
            "m3": num_units + 3
        })

    def _cell(i):
        exit(rnn_cell.LSTMCell(
            num_units + i,
            use_peepholes=False,
            initializer=initializer,
            state_is_tuple=True))

    # This creates a state tuple which has 4 sub-tuples of length 2 each.
    cell = rnn_cell.MultiRNNCell(
        [_cell(i) for i in range(4)], state_is_tuple=True)

    self.assertEqual(len(cell.state_size), 4)
    for i in range(4):
        self.assertEqual(len(cell.state_size[i]), 2)

    inputs = max_length * [
        array_ops.placeholder(dtypes.float32, shape=(batch_size, input_size))
    ]

    state_names = (("c0", "m0"), ("c1", "m1"), ("c2", "m2"), ("c3", "m3"))
    with variable_scope.variable_scope("share_scope"):
        outputs, state = rnn.static_state_saving_rnn(
            cell, inputs, state_saver=state_saver, state_name=state_names)
    self.assertEqual(len(outputs), len(inputs))

    # Final output comes from _cell(3) which has state size num_units + 3
    for out in outputs:
        self.assertEqual(out.get_shape().as_list(), [batch_size, num_units + 3])

    variables_lib.global_variables_initializer().run()
    input_value = np.random.randn(batch_size, input_size)
    last_states = sess.run(
        list(nest.flatten(state)), feed_dict={
            inputs[0]: input_value
        })
    saved_states = sess.run(
        list(state_saver.saved_state.values()),
        feed_dict={
            inputs[0]: input_value
        })
    self.assertEqual(8, len(last_states))
    self.assertEqual(8, len(saved_states))
    flat_state_names = nest.flatten(state_names)
    named_saved_states = dict(
        zip(state_saver.saved_state.keys(), saved_states))

    for i in range(8):
        self.assertAllEqual(last_states[i],
                            named_saved_states[flat_state_names[i]])
