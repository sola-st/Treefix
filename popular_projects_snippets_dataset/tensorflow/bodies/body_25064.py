# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_grappler_test.py
"""Tests that tfdbg can dump the tensor from nodes created by Grappler."""
with session.Session(config=_grappler_enabled_session_config()) as sess:
    u = variables.VariableV1([[1, 2], [3, 4]], name="u", dtype=dtypes.float32)
    # The next two ops should be optimized by Grappler into a single op:
    # either an AddN op or a Mul op.
    x = math_ops.add(u, u)
    x = math_ops.add(x, u)
    y = math_ops.multiply(x, u)

    sess.run(variables.global_variables_initializer())

    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    debug_utils.watch_graph(
        run_options,
        sess.graph,
        debug_ops=["DebugIdentity"],
        debug_urls=[self._debug_url])

    run_metadata = config_pb2.RunMetadata()
    run_result = sess.run(y, options=run_options, run_metadata=run_metadata)
    self.assertAllClose(run_result, [[3, 12], [27, 48]])

    dump_data = debug_data.DebugDumpDir(
        self._dump_root, partition_graphs=run_metadata.partition_graphs,
        validate=True)

    original_node_names = set(op.name for op in sess.graph.get_operations())
    dumped_node_names = set(dump_data.nodes())
    grappler_created_node_names = dumped_node_names - original_node_names
    grappler_removed_node_names = original_node_names - dumped_node_names

    # Assert that Grappler should have replaced some of the nodes from the
    # original graph with new nodes.
    self.assertTrue(grappler_created_node_names)
    self.assertTrue(grappler_removed_node_names)

    # Iterate through the nodes created by Grappler. One of them should be
    # be the result of replacing the original add ops with an AddN op or a
    # Mul op.
    found_optimized_node = False
    for grappler_node_name in grappler_created_node_names:
        node_op_type = dump_data.node_op_type(grappler_node_name)
        # Look for the node created by Grappler's arithmetic optimization.
        if ((test_util.IsMklEnabled() and node_op_type in ("_MklAddN", "Mul"))
            or (node_op_type in ("AddN", "Mul"))):
            datum = dump_data.get_tensors(grappler_node_name, 0, "DebugIdentity")
            self.assertEqual(1, len(datum))
            self.assertAllClose(datum[0], [[3, 6], [9, 12]])
            found_optimized_node = True
            break
    self.assertTrue(
        found_optimized_node,
        "Failed to find optimized node created by Grappler's arithmetic "
        "optimization.")
