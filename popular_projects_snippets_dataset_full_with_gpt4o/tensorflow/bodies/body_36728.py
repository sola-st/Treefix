# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
with self.session(graph=ops.Graph()) as sess:
    # Build the cond_v2 in an XLA context
    xla_context = control_flow_ops.XLAControlFlowContext()
    xla_context.Enter()
    cond_output, cond_op = self._createCond("cond")
    xla_context.Exit()

    # Check lowering attr is not set.
    with self.assertRaises(ValueError):
        cond_op.get_attr("_lower_using_switch_merge")

    # Check the actual graph that is run.
    run_options = config_pb2.RunOptions(output_partition_graphs=True)
    run_metadata = config_pb2.RunMetadata()
    sess.run(cond_output, options=run_options, run_metadata=run_metadata)

    # Lowering disabled in XLA, there should be no `Switch` node
    self.assertFalse(
        _has_node_with_op(run_metadata, "Switch"),
        "A `Switch` op exists, but the graph should not be lowered.")

    if test_util.is_xla_enabled():
        # If XLA is actually enabled then we expect the StatelessIf to have been
        # put inside an XLA cluster.
        self.assertFalse(
            _has_node_with_op(run_metadata, "StatelessIf"),
            ("A `StatelessIf` op was found, but the node should have been " +
             "clustered."))
        self.assertTrue(
            _has_node_with_op(run_metadata, "_XlaCompile"),
            ("An `_XlaCompile` op was not found, but the `StatelessIf` (at " +
             "least) op should have been clustered."))
        self.assertTrue(
            _has_node_with_op(run_metadata, "_XlaRun"),
            ("An `_XlaRun` op was not found, but the `StatelessIf` (at " +
             "least) op should have been clustered."))
    else:
        # Lowering disabled in XLA, there should still be an `If` node
        self.assertTrue(
            _has_node_with_op(run_metadata, "StatelessIf"),
            ("A `StatelessIf` op was not found, but the graph should not be " +
             "lowered."))
