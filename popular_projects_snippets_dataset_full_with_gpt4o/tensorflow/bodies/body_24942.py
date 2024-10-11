# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_utils_test.py
debug_utils.watch_graph(
    self._run_options,
    self._graph,
    debug_urls="file:///tmp/tfdbg_1",
    node_name_regex_allowlist="(a1$|a1_init$|a1/.*|p1$)")

node_names = self._verify_watches(
    self._run_options.debug_options.debug_tensor_watch_opts, 0,
    ["DebugIdentity"], ["file:///tmp/tfdbg_1"])
self.assertEqual(
    sorted(["a1_init", "a1", "a1/Assign", "a1/read", "p1"]),
    sorted(node_names))
