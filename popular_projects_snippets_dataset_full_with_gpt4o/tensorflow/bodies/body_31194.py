# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
"""Smoke test for using LSTM with doubles, dropout, dynamic calculation."""

num_units = 3
input_size = 5
batch_size = 2
num_proj = 4
num_proj_shards = 3
num_unit_shards = 2
max_length = 8
with self.session(graph=ops.Graph()) as sess:
    sequence_length = array_ops.placeholder(dtypes.int64)
    initializer = init_ops.random_uniform_initializer(
        -0.01, 0.01, seed=self._seed)
    inputs = max_length * [
        array_ops.placeholder(dtypes.float64, shape=(None, input_size))
    ]

    cell = rnn_cell.LSTMCell(
        num_units,
        use_peepholes=True,
        num_proj=num_proj,
        num_unit_shards=num_unit_shards,
        num_proj_shards=num_proj_shards,
        initializer=initializer,
        state_is_tuple=False)
    dropout_cell = rnn_cell.DropoutWrapper(cell, 0.5, seed=0)

    outputs, state = rnn.static_rnn(
        dropout_cell,
        inputs,
        sequence_length=sequence_length,
        initial_state=cell.zero_state(batch_size, dtypes.float64))

    self.assertEqual(len(outputs), len(inputs))

    variables_lib.global_variables_initializer().run(feed_dict={
        sequence_length: [2, 3]
    })
    input_value = np.asarray(
        np.random.randn(batch_size, input_size), dtype=np.float64)
    values = sess.run(
        outputs, feed_dict={
            inputs[0]: input_value,
            sequence_length: [2, 3]
        })
    state_value = sess.run(
        [state], feed_dict={
            inputs[0]: input_value,
            sequence_length: [2, 3]
        })
    self.assertEqual(values[0].dtype, input_value.dtype)
    self.assertEqual(state_value[0].dtype, input_value.dtype)
