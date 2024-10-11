# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_utils_test.py
debug_utils.watch_graph_with_denylists(
    self._run_options,
    self._graph,
    debug_urls="file:///tmp/tfdbg_1",
    node_name_regex_denylist="p1$",
    op_type_regex_denylist="(Variable|Identity|Assign|Const)")

node_names = self._verify_watches(
    self._run_options.debug_options.debug_tensor_watch_opts, 0,
    ["DebugIdentity"], ["file:///tmp/tfdbg_1"])
self.assertEqual(["s"], node_names)
