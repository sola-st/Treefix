# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
with ops.Graph().as_default() as g:
    # Disable Loop_optimizer grappler pass for this test because it replaces
    # Switch with Identity when it's part of a dead branch.
    config = config_pb2.ConfigProto()
    config.graph_options.rewrite_options.loop_optimization = (
        rewriter_config_pb2.RewriterConfig.OFF)
    with self.session(graph=g, config=config) as sess:
        cond_output, _ = self._createCond("cond")

        run_options = config_pb2.RunOptions(output_partition_graphs=True)
        run_metadata = config_pb2.RunMetadata()
        sess.run(cond_output, options=run_options, run_metadata=run_metadata)

        # If lowering was enabled, there should be a `Switch` node
        self.assertTrue(
            _has_node_with_op(run_metadata, "Switch"),
            "A `Switch` op should exist if the graph was lowered.")

        # If lowering was enabled, there should be no `If` node
        self.assertFalse(
            _has_node_with_op(run_metadata, "StatelessIf"),
            "An `If` op was found, but it should be lowered.")
