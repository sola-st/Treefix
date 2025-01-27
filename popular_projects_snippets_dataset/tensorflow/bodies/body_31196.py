# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
num_units = 3
input_size = 5
batch_size = 2
num_proj = 4
max_length = 8
with self.session(graph=ops.Graph()) as sess:
    initializer = init_ops.random_uniform_initializer(-1, 1, seed=self._seed)
    inputs = max_length * [
        array_ops.placeholder(dtypes.float32, shape=(None, input_size))
    ]
    cell = rnn_cell.LSTMCell(
        num_units,
        use_peepholes=True,
        num_proj=num_proj,
        initializer=initializer,
        state_is_tuple=False)

    with ops.name_scope("scope0"):
        with variable_scope.variable_scope("share_scope"):
            outputs0, _ = rnn.static_rnn(cell, inputs, dtype=dtypes.float32)
    with ops.name_scope("scope1"):
        with variable_scope.variable_scope("share_scope", reuse=True):
            outputs1, _ = rnn.static_rnn(cell, inputs, dtype=dtypes.float32)

    variables_lib.global_variables_initializer().run()
    input_value = np.random.randn(batch_size, input_size)
    output_values = sess.run(
        outputs0 + outputs1, feed_dict={
            inputs[0]: input_value
        })
    outputs0_values = output_values[:max_length]
    outputs1_values = output_values[max_length:]
    self.assertEqual(len(outputs0_values), len(outputs1_values))
    for out0, out1 in zip(outputs0_values, outputs1_values):
        self.assertAllEqual(out0, out1)
