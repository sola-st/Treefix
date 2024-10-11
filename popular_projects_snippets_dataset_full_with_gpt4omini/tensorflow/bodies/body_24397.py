# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
with session.Session() as sess:
    input_size = 3
    state_size = 2
    time_steps = 4
    batch_size = 2

    input_values = np.random.randn(time_steps, batch_size, input_size)
    sequence_length = np.random.randint(0, time_steps, size=batch_size)
    concat_inputs = array_ops.placeholder(
        dtypes.float32, shape=(time_steps, batch_size, input_size))

    outputs_dynamic, _ = rnn.dynamic_rnn(
        _RNNCellForTest(input_size, state_size),
        inputs=concat_inputs,
        sequence_length=sequence_length,
        time_major=True,
        dtype=dtypes.float32)
    toy_loss = math_ops.reduce_sum(outputs_dynamic * outputs_dynamic)
    train_op = gradient_descent.GradientDescentOptimizer(
        learning_rate=0.1).minimize(toy_loss, name="train_op")

    sess.run(variables.global_variables_initializer())

    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_utils.watch_graph_with_denylists(
        run_options,
        sess.graph,
        node_name_regex_denylist="(.*rnn/while/.*|.*TensorArray.*)",
        debug_urls=self._debug_urls())
    # b/36870549: Nodes with these name patterns need to be excluded from
    # tfdbg in order to prevent MSAN warnings of uninitialized Tensors
    # under both file:// and grpc:// debug URL schemes.

    run_metadata = config_pb2.RunMetadata()
    sess.run(train_op, feed_dict={concat_inputs: input_values},
             options=run_options, run_metadata=run_metadata)

    debug_data.DebugDumpDir(
        self._dump_root, partition_graphs=run_metadata.partition_graphs)
