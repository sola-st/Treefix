# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
num_units = 3
input_size = 5
batch_size = 2
num_proj = 4
max_length = 8
sequence_length = [4, 6]
with self.session(graph=ops.Graph()) as sess:
    initializer = init_ops.random_uniform_initializer(
        -0.01, 0.01, seed=self._seed)
    inputs = max_length * [
        array_ops.placeholder(dtypes.float32, shape=(None, input_size))
    ]
    cell_notuple = rnn_cell.LSTMCell(
        num_units,
        use_peepholes=True,
        num_proj=num_proj,
        initializer=initializer,
        state_is_tuple=False)
    cell_tuple = rnn_cell.LSTMCell(
        num_units,
        use_peepholes=True,
        num_proj=num_proj,
        initializer=initializer,
        state_is_tuple=True)
    with variable_scope.variable_scope("root") as scope:
        outputs_notuple, state_notuple = rnn.static_rnn(
            cell_notuple,
            inputs,
            dtype=dtypes.float32,
            sequence_length=sequence_length,
            scope=scope)
        scope.reuse_variables()
        # TODO(ebrevdo): For this test, we ensure values are identical and
        # therefore the weights here are tied.  In the future, we may consider
        # making the state_is_tuple property mutable so we can avoid
        # having to do this - especially if users ever need to reuse
        # the parameters from different RNNCell instances.  Right now,
        # this seems an unrealistic use case except for testing.
        cell_tuple._scope = cell_notuple._scope  # pylint: disable=protected-access
        outputs_tuple, state_tuple = rnn.static_rnn(
            cell_tuple,
            inputs,
            dtype=dtypes.float32,
            sequence_length=sequence_length,
            scope=scope)
    self.assertEqual(len(outputs_notuple), len(inputs))
    self.assertEqual(len(outputs_tuple), len(inputs))
    self.assertTrue(isinstance(state_tuple, tuple))
    self.assertTrue(isinstance(state_notuple, ops.Tensor))

    variables_lib.global_variables_initializer().run()
    input_value = np.random.randn(batch_size, input_size)
    outputs_notuple_v = sess.run(
        outputs_notuple, feed_dict={
            inputs[0]: input_value
        })
    outputs_tuple_v = sess.run(
        outputs_tuple, feed_dict={
            inputs[0]: input_value
        })
    self.assertAllEqual(outputs_notuple_v, outputs_tuple_v)

    (state_notuple_v,) = sess.run(
        (state_notuple,), feed_dict={
            inputs[0]: input_value
        })
    state_tuple_v = sess.run(state_tuple, feed_dict={inputs[0]: input_value})
    self.assertAllEqual(state_notuple_v, np.hstack(state_tuple_v))
