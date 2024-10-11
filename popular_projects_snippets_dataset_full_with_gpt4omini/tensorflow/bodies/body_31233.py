# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
time_steps = 8
num_units = 3
input_size = 5
batch_size = 2

input_values = np.random.randn(time_steps, batch_size, input_size)

sequence_length = np.random.randint(0, time_steps, size=batch_size)

with self.session(graph=ops.Graph()) as sess:
    concat_inputs = array_ops.placeholder(
        dtypes.float32, shape=(time_steps, batch_size, input_size))

    cell = rnn_cell.GRUCell(num_units=num_units)

    with variable_scope.variable_scope("dynamic_scope"):
        outputs_dynamic, state_dynamic = rnn.dynamic_rnn(
            cell,
            inputs=concat_inputs,
            sequence_length=sequence_length,
            time_major=True,
            dtype=dtypes.float32)

    feeds = {concat_inputs: input_values}

    # Initialize
    variables_lib.global_variables_initializer().run(feed_dict=feeds)

    sess.run([outputs_dynamic, state_dynamic], feed_dict=feeds)
