# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_utils_test.py
debug_utils.watch_graph(
    self._run_options,
    self._graph,
    debug_ops=["DebugIdentity", "DebugNanCount"],
    debug_urls="file:///tmp/tfdbg_1")

debug_watch_opts = self._run_options.debug_options.debug_tensor_watch_opts
self.assertEqual(self._expected_num_nodes, len(debug_watch_opts))

# Verify that each of the nodes in the graph with output tensors in the
# graph have debug tensor watch.
node_names = self._verify_watches(debug_watch_opts, 0,
                                  ["DebugIdentity", "DebugNanCount"],
                                  ["file:///tmp/tfdbg_1"])

# Verify the node names.
self.assertIn("a1_init", node_names)
self.assertIn("a1", node_names)
self.assertIn("a1/Assign", node_names)
self.assertIn("a1/read", node_names)

self.assertIn("b_init", node_names)
self.assertIn("b", node_names)
self.assertIn("b/Assign", node_names)
self.assertIn("b/read", node_names)

self.assertIn("c", node_names)
self.assertIn("p1", node_names)
self.assertIn("s", node_names)

# Assert that the wildcard node name has been created.
self.assertIn("*", node_names)
