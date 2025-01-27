# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
num_units = 3
input_size = 5
batch_size = 2
num_proj = 4
max_length = 8
with self.session(graph=ops.Graph()) as sess:
    initializer = init_ops.random_uniform_initializer(
        -0.01, 0.01, seed=self._seed)
    inputs = max_length * [
        array_ops.placeholder(dtypes.float32, shape=(None, input_size))
    ]
    cell = rnn_cell.LSTMCell(
        num_units,
        use_peepholes=True,
        num_proj=num_proj,
        initializer=initializer,
        state_is_tuple=False)
    outputs, _ = rnn.static_rnn(cell, inputs, dtype=dtypes.float32)
    self.assertEqual(len(outputs), len(inputs))

    variables_lib.global_variables_initializer().run()
    input_value = np.random.randn(batch_size, input_size)
    sess.run(outputs, feed_dict={inputs[0]: input_value})
