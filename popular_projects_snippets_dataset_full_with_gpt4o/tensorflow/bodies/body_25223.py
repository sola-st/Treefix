# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
"""List an input tree containing tensors from non-:0 output slot."""

with session.Session(config=no_rewrite_session_config()) as sess:
    with ops.device("CPU:0"):
        x = variables.VariableV1([1, 3, 3, 7], name="x")
        _, idx = array_ops.unique(x, name="x_unique")
        idx_times_two = math_ops.multiply(idx, 2, name="idx_times_two")
        self.evaluate(x.initializer)

        run_options = config_pb2.RunOptions(output_partition_graphs=True)
        debug_utils.watch_graph(
            run_options,
            sess.graph,
            debug_ops=["DebugIdentity"],
            debug_urls="file://%s" % self._dump_root_for_unique)
        run_metadata = config_pb2.RunMetadata()
        self.assertAllEqual([0, 2, 2, 4],
                            sess.run(
                                idx_times_two,
                                options=run_options,
                                run_metadata=run_metadata))
        debug_dump = debug_data.DebugDumpDir(
            self._dump_root_for_unique,
            partition_graphs=run_metadata.partition_graphs)
        _, registry = create_analyzer_cli(debug_dump)

        out = registry.dispatch_command("li", ["idx_times_two"])
        self.assertEqual([
            "Inputs to node \"idx_times_two\" (Depth limit = 1):",
            "|- (1) x_unique:1"
        ], out.lines[:2])
