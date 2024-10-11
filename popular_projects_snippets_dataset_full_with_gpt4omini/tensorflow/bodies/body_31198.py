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
    cell = rnn_cell.LSTMCell(
        num_units,
        use_peepholes=True,
        num_proj=num_proj,
        initializer=initializer,
        state_is_tuple=True)
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
    self.assertTrue(isinstance(state_static, rnn_cell.LSTMStateTuple))
    self.assertTrue(isinstance(state_dynamic, rnn_cell.LSTMStateTuple))
    self.assertIs(state_static[0], state_static.c)
    self.assertIs(state_static[1], state_static.h)
    self.assertIs(state_dynamic[0], state_dynamic.c)
    self.assertIs(state_dynamic[1], state_dynamic.h)

    if in_graph_mode:
        variables_lib.global_variables_initializer().run()
        input_value = np.random.randn(batch_size, input_size)
        outputs_static = sess.run(
            outputs_static, feed_dict={
                inputs[0]: input_value
            })
        outputs_dynamic = sess.run(
            outputs_dynamic, feed_dict={
                inputs[0]: input_value
            })
        state_static = sess.run(
            state_static, feed_dict={
                inputs[0]: input_value
            })
        state_dynamic = sess.run(
            state_dynamic, feed_dict={
                inputs[0]: input_value
            })

    comparison_fn = self.assertAllEqual
    if test_util.is_xla_enabled():
        comparison_fn = self.assertAllClose
    if in_graph_mode:
        comparison_fn(outputs_static, outputs_dynamic)
    else:
        self.assertAllEqual(array_ops.stack(outputs_static), outputs_dynamic)
    comparison_fn(np.hstack(state_static), np.hstack(state_dynamic))
