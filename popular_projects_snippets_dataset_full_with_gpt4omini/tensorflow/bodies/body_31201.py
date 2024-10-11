# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
time_steps = 8
num_units = 3
num_proj = 4
input_size = 5
batch_size = 2

input_values = np.random.randn(time_steps, batch_size, input_size).astype(
    np.float32)

if use_sequence_length:
    sequence_length = np.random.randint(0, time_steps, size=batch_size)
else:
    sequence_length = None

in_graph_mode = not context.executing_eagerly()

# TODO(b/68017812): Eager ignores operation seeds, so we need to create a
# single cell and reuse it across the static and dynamic RNNs. Remove this
# special case once is fixed.
if not in_graph_mode:
    initializer = init_ops.random_uniform_initializer(
        -0.01, 0.01, seed=self._seed)
    cell = rnn_cell.LSTMCell(
        num_units,
        use_peepholes=True,
        initializer=initializer,
        num_proj=num_proj,
        state_is_tuple=False)

########### Step 1: Run static graph and generate readouts
with self.session(graph=ops.Graph()) as sess:
    if in_graph_mode:
        concat_inputs = array_ops.placeholder(
            dtypes.float32, shape=(time_steps, batch_size, input_size))
    else:
        concat_inputs = constant_op.constant(input_values)
    inputs = array_ops.unstack(concat_inputs)
    initializer = init_ops.random_uniform_initializer(
        -0.01, 0.01, seed=self._seed)

    # TODO(akshayka): Remove special case once b/68017812 is fixed.
    if in_graph_mode:
        cell = rnn_cell.LSTMCell(
            num_units,
            use_peepholes=True,
            initializer=initializer,
            num_proj=num_proj,
            state_is_tuple=False)

    with variable_scope.variable_scope("dynamic_scope"):
        outputs_static, state_static = rnn.static_rnn(
            cell, inputs, sequence_length=sequence_length, dtype=dtypes.float32)

    if in_graph_mode:
        # Generate gradients of sum of outputs w.r.t. inputs
        static_gradients = gradients_impl.gradients(
            outputs_static + [state_static], [concat_inputs])
        # Generate gradients of individual outputs w.r.t. inputs
        static_individual_gradients = nest.flatten([
            gradients_impl.gradients(y, [concat_inputs])
            for y in [outputs_static[0], outputs_static[-1], state_static]
        ])
        # Generate gradients of individual variables w.r.t. inputs
        trainable_variables = ops.get_collection(
            ops.GraphKeys.TRAINABLE_VARIABLES)
        assert len(trainable_variables) > 1, (
            "Count of trainable variables: %d" % len(trainable_variables))
        # pylint: disable=bad-builtin
        static_individual_variable_gradients = nest.flatten([
            gradients_impl.gradients(y, trainable_variables)
            for y in [outputs_static[0], outputs_static[-1], state_static]
        ])
        # Generate gradients and run sessions to obtain outputs
        feeds = {concat_inputs: input_values}
        # Initialize
        variables_lib.global_variables_initializer().run(feed_dict=feeds)
        # Test forward pass
        values_static = sess.run(outputs_static, feed_dict=feeds)
        (state_value_static,) = sess.run((state_static,), feed_dict=feeds)

        # Test gradients to inputs and variables w.r.t. outputs & final state
        static_grad_values = sess.run(static_gradients, feed_dict=feeds)

        static_individual_grad_values = sess.run(
            static_individual_gradients, feed_dict=feeds)

        static_individual_var_grad_values = sess.run(
            static_individual_variable_gradients, feed_dict=feeds)

    ########## Step 2: Run dynamic graph and generate readouts
with self.session(graph=ops.Graph()) as sess:
    if in_graph_mode:
        concat_inputs = array_ops.placeholder(
            dtypes.float32, shape=(time_steps, batch_size, input_size))
    else:
        concat_inputs = constant_op.constant(input_values)
    initializer = init_ops.random_uniform_initializer(
        -0.01, 0.01, seed=self._seed)

    # TODO(akshayka): Remove this special case once b/68017812 is
    # fixed.
    if in_graph_mode:
        cell = rnn_cell.LSTMCell(
            num_units,
            use_peepholes=True,
            initializer=initializer,
            num_proj=num_proj,
            state_is_tuple=False)

    with variable_scope.variable_scope("dynamic_scope"):
        outputs_dynamic, state_dynamic = rnn.dynamic_rnn(
            cell,
            inputs=concat_inputs,
            sequence_length=sequence_length,
            time_major=True,
            dtype=dtypes.float32)
        split_outputs_dynamic = array_ops.unstack(outputs_dynamic, time_steps)

    if in_graph_mode:

        # Generate gradients of sum of outputs w.r.t. inputs
        dynamic_gradients = gradients_impl.gradients(
            split_outputs_dynamic + [state_dynamic], [concat_inputs])

        # Generate gradients of several individual outputs w.r.t. inputs
        dynamic_individual_gradients = nest.flatten([
            gradients_impl.gradients(y, [concat_inputs])
            for y in [
                split_outputs_dynamic[0], split_outputs_dynamic[-1],
                state_dynamic
            ]
        ])

        # Generate gradients of individual variables w.r.t. inputs
        trainable_variables = ops.get_collection(
            ops.GraphKeys.TRAINABLE_VARIABLES)
        assert len(trainable_variables) > 1, (
            "Count of trainable variables: %d" % len(trainable_variables))
        dynamic_individual_variable_gradients = nest.flatten([
            gradients_impl.gradients(y, trainable_variables)
            for y in [
                split_outputs_dynamic[0], split_outputs_dynamic[-1],
                state_dynamic
            ]
        ])

        feeds = {concat_inputs: input_values}

        # Initialize
        variables_lib.global_variables_initializer().run(feed_dict=feeds)

        # Test forward pass
        values_dynamic = sess.run(split_outputs_dynamic, feed_dict=feeds)
        (state_value_dynamic,) = sess.run((state_dynamic,), feed_dict=feeds)

        # Test gradients to inputs and variables w.r.t. outputs & final state
        dynamic_grad_values = sess.run(dynamic_gradients, feed_dict=feeds)

        dynamic_individual_grad_values = sess.run(
            dynamic_individual_gradients, feed_dict=feeds)

        dynamic_individual_var_grad_values = sess.run(
            dynamic_individual_variable_gradients, feed_dict=feeds)

    ######### Step 3: Comparisons
if not in_graph_mode:
    values_static = outputs_static
    values_dynamic = split_outputs_dynamic
    state_value_static = state_static
    state_value_dynamic = state_dynamic

self.assertEqual(len(values_static), len(values_dynamic))
for (value_static, value_dynamic) in zip(values_static, values_dynamic):
    self.assertAllClose(value_static, value_dynamic)
self.assertAllClose(state_value_static, state_value_dynamic)

if in_graph_mode:

    self.assertAllClose(static_grad_values, dynamic_grad_values)

    self.assertEqual(
        len(static_individual_grad_values),
        len(dynamic_individual_grad_values))
    self.assertEqual(
        len(static_individual_var_grad_values),
        len(dynamic_individual_var_grad_values))

    for i, (a, b) in enumerate(
        zip(static_individual_grad_values, dynamic_individual_grad_values)):
        tf_logging.info("Comparing individual gradients iteration %d" % i)
        self.assertAllClose(a, b)

    for i, (a, b) in enumerate(
        zip(static_individual_var_grad_values,
            dynamic_individual_var_grad_values)):
        tf_logging.info(
            "Comparing individual variable gradients iteration %d" % i)
        self.assertAllClose(a, b)
