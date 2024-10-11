# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
num_units = 3
input_size = 5
batch_size = 2
num_proj = 4
num_proj_shards = 3
num_unit_shards = 2
max_length = 8
with self.session(graph=ops.Graph()) as sess:
    inputs = max_length * [
        array_ops.placeholder(dtypes.float32, shape=(None, input_size))
    ]
    initializer = init_ops.constant_initializer(0.001)

    cell_noshard = rnn_cell.LSTMCell(
        num_units,
        num_proj=num_proj,
        use_peepholes=True,
        initializer=initializer,
        num_unit_shards=num_unit_shards,
        num_proj_shards=num_proj_shards,
        state_is_tuple=False)

    cell_shard = rnn_cell.LSTMCell(
        num_units,
        use_peepholes=True,
        initializer=initializer,
        num_proj=num_proj,
        state_is_tuple=False)

    with variable_scope.variable_scope("noshard_scope"):
        outputs_noshard, state_noshard = rnn.static_rnn(
            cell_noshard, inputs, dtype=dtypes.float32)
    with variable_scope.variable_scope("shard_scope"):
        outputs_shard, state_shard = rnn.static_rnn(
            cell_shard, inputs, dtype=dtypes.float32)

    self.assertEqual(len(outputs_noshard), len(inputs))
    self.assertEqual(len(outputs_noshard), len(outputs_shard))

    variables_lib.global_variables_initializer().run()
    input_value = np.random.randn(batch_size, input_size)
    feeds = dict((x, input_value) for x in inputs)
    values_noshard = sess.run(outputs_noshard, feed_dict=feeds)
    values_shard = sess.run(outputs_shard, feed_dict=feeds)
    state_values_noshard = sess.run([state_noshard], feed_dict=feeds)
    state_values_shard = sess.run([state_shard], feed_dict=feeds)
    self.assertEqual(len(values_noshard), len(values_shard))
    self.assertEqual(len(state_values_noshard), len(state_values_shard))
    for (v_noshard, v_shard) in zip(values_noshard, values_shard):
        self.assertAllClose(v_noshard, v_shard, atol=1e-3)
    for (s_noshard, s_shard) in zip(state_values_noshard, state_values_shard):
        self.assertAllClose(s_noshard, s_shard, atol=1e-3)
