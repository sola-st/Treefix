# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
num_units = 3
input_size = 5
batch_size = 2
max_length = 8
with self.session(graph=ops.Graph()) as sess:
    initializer = init_ops.random_uniform_initializer(
        -0.01, 0.01, seed=self._seed)
    cell = rnn_cell.LSTMCell(
        num_units,
        use_peepholes=True,
        cell_clip=0.0,
        initializer=initializer,
        state_is_tuple=False)
    inputs = max_length * [
        array_ops.placeholder(dtypes.float32, shape=(batch_size, input_size))
    ]
    outputs, _ = rnn.static_rnn(cell, inputs, dtype=dtypes.float32)
    self.assertEqual(len(outputs), len(inputs))
    for out in outputs:
        self.assertEqual(out.get_shape().as_list(), [batch_size, num_units])

    variables_lib.global_variables_initializer().run()
    input_value = np.random.randn(batch_size, input_size)
    values = sess.run(outputs, feed_dict={inputs[0]: input_value})

for value in values:
    # if cell c is clipped to 0, tanh(c) = 0 => m==0
    self.assertAllEqual(value, np.zeros((batch_size, num_units)))
