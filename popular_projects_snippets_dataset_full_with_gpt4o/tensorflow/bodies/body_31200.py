# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
num_units = 3
input_size = 5
batch_size = 2
num_proj = 4
max_length = 8
sequence_length = [4, 6]
in_graph_mode = not context.executing_eagerly()
with self.session(graph=ops.Graph()) as sess:
    initializer = init_ops.random_uniform_initializer(
        -0.01, 0.01, seed=self._seed)
    if in_graph_mode:
        inputs = max_length * [
            array_ops.placeholder(dtypes.float32, shape=(None, input_size))
        ]
    else:
        inputs = max_length * [
            constant_op.constant(
                np.random.randn(batch_size, input_size).astype(np.float32))
        ]
    inputs_c = array_ops.stack(inputs)

    def _cell(i):
        exit(rnn_cell.LSTMCell(
            num_units + i,
            use_peepholes=True,
            num_proj=num_proj + i,
            initializer=initializer,
            state_is_tuple=True))

    # This creates a state tuple which has 4 sub-tuples of length 2 each.
    cell = rnn_cell.MultiRNNCell(
        [_cell(i) for i in range(4)], state_is_tuple=True)

    self.assertEqual(len(cell.state_size), 4)
    for i in range(4):
        self.assertEqual(len(cell.state_size[i]), 2)

    test_zero = cell.zero_state(1, dtypes.float32)
    self.assertEqual(len(test_zero), 4)
    for i in range(4):
        self.assertEqual(test_zero[i][0].get_shape()[1], cell.state_size[i][0])
        self.assertEqual(test_zero[i][1].get_shape()[1], cell.state_size[i][1])

    with variable_scope.variable_scope("root") as scope:
        outputs_static, state_static = rnn.static_rnn(
            cell,
            inputs,
            dtype=dtypes.float32,
            sequence_length=sequence_length,
            scope=scope)
        scope.reuse_variables()
        outputs_dynamic, state_dynamic = rnn.dynamic_rnn(
            cell,
            inputs_c,
            dtype=dtypes.float32,
            time_major=True,
            sequence_length=sequence_length,
            scope=scope)

    if in_graph_mode:
        input_value = np.random.randn(batch_size, input_size)
        variables_lib.global_variables_initializer().run()
        outputs_static = sess.run(
            outputs_static, feed_dict={
                inputs[0]: input_value
            })
        outputs_dynamic = sess.run(
            outputs_dynamic, feed_dict={
                inputs[0]: input_value
            })
        state_static = sess.run(
            nest.flatten(state_static), feed_dict={
                inputs[0]: input_value
            })
        state_dynamic = sess.run(
            nest.flatten(state_dynamic), feed_dict={
                inputs[0]: input_value
            })

    comparison_fn = self.assertAllEqual
    if test_util.is_xla_enabled():
        comparison_fn = self.assertAllClose
    if in_graph_mode:
        comparison_fn(outputs_static, outputs_dynamic)
    else:
        self.assertAllEqual(array_ops.stack(outputs_static), outputs_dynamic)
        state_static = nest.flatten(state_static)
        state_dynamic = nest.flatten(state_dynamic)
    comparison_fn(np.hstack(state_static), np.hstack(state_dynamic))
