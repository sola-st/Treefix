# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graph_reconstruction_test.py
run_options = config_pb2.RunOptions(output_partition_graphs=True)
run_metadata = config_pb2.RunMetadata()
output = sess.run(fetches, feed_dict=feed_dict, options=run_options,
                  run_metadata=run_metadata)
if expected_output is not None:
    self.assertAllClose(expected_output, output)
non_debug_graph_defs = run_metadata.partition_graphs

debug_utils.watch_graph(
    run_options, sess.graph, debug_urls=self._debug_url)
run_metadata = config_pb2.RunMetadata()
output = sess.run(fetches, feed_dict=feed_dict, options=run_options,
                  run_metadata=run_metadata)
if expected_output is not None:
    self.assertAllClose(expected_output, output)

dump = debug_data.DebugDumpDir(
    self._dump_dir, partition_graphs=run_metadata.partition_graphs,
    validate=True)
reconstructed = dump.reconstructed_non_debug_partition_graphs()

self.assertEqual(len(non_debug_graph_defs), len(reconstructed))
for i, non_debug_graph_def in enumerate(non_debug_graph_defs):
    device_name = debug_graphs._infer_device_name(non_debug_graph_def)
    test_util.assert_equal_graph_def(
        self._graphDefWithoutDenylistedNodes(reconstructed[device_name]),
        self._graphDefWithoutDenylistedNodes(non_debug_graph_def))

    # Test debug_graphs.reconstruct_non_debug_graph_def.
    reconstructed_again = (
        debug_graphs.reconstruct_non_debug_graph_def(
            run_metadata.partition_graphs[i]))
    test_util.assert_equal_graph_def(
        self._graphDefWithoutDenylistedNodes(reconstructed_again),
        self._graphDefWithoutDenylistedNodes(non_debug_graph_def))
