# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
self.assertEqual(
    (["node_a:1", "node_a:2", "node_b:1", "node_b:2"], "node_"),
    self._tc_reg.get_completions("print_tensor", "node_"))
self.assertEqual((["node_a", "node_b", "node_c"], "node_"),
                 self._tc_reg.get_completions("node_info", "node_"))

self._tc_reg.extend_comp_items("print_tensor", ["node_A:1", "node_A:2"])

self.assertEqual((["node_A:1", "node_A:2", "node_a:1", "node_a:2",
                   "node_b:1", "node_b:2"], "node_"),
                 self._tc_reg.get_completions("print_tensor", "node_"))

# Extending the completions for one of the context's context words should
# have taken effect on other context words of the same context as well.
self.assertEqual((["node_A:1", "node_A:2", "node_a:1", "node_a:2",
                   "node_b:1", "node_b:2"], "node_"),
                 self._tc_reg.get_completions("pt", "node_"))
self.assertEqual((["node_a", "node_b", "node_c"], "node_"),
                 self._tc_reg.get_completions("node_info", "node_"))
