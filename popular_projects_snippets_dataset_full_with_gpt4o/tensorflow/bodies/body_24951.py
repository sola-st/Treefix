# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_utils_test.py
debug_utils.watch_graph_with_denylists(
    self._run_options,
    self._graph,
    debug_urls="file:///tmp/tfdbg_1",
    node_name_regex_denylist="^s$",
    tensor_dtype_regex_denylist=".*_ref")

node_names = self._verify_watches(
    self._run_options.debug_options.debug_tensor_watch_opts, 0,
    ["DebugIdentity"], ["file:///tmp/tfdbg_1"])
self.assertNotIn("a1", node_names)
self.assertNotIn("a1/Assign", node_names)
self.assertNotIn("b", node_names)
self.assertNotIn("b/Assign", node_names)
self.assertNotIn("s", node_names)
