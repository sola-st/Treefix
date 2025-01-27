# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_utils_test.py
debug_utils.watch_graph(
    self._run_options,
    self._graph,
    debug_urls="file:///tmp/tfdbg_1",
    tensor_dtype_regex_allowlist=".*_ref")

node_names = self._verify_watches(
    self._run_options.debug_options.debug_tensor_watch_opts, 0,
    ["DebugIdentity"], ["file:///tmp/tfdbg_1"])
self.assertItemsEqual(["a1", "a1/Assign", "b", "b/Assign"], node_names)
