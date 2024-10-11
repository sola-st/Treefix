# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
self.assertEqual(
    (["node_a:1", "node_a:2", "node_b:1", "node_b:2"], "node_"),
    self._tc_reg.get_completions("print_tensor", "node_"))
self.assertEqual((["node_a", "node_b", "node_c"], "node_"),
                 self._tc_reg.get_completions("node_info", "node_"))

self._tc_reg.deregister_context(["print_tensor"])

self.assertEqual((None, None),
                 self._tc_reg.get_completions("print_tensor", "node_"))

# The alternative context word should be unaffected.
self.assertEqual(
    (["node_a:1", "node_a:2", "node_b:1", "node_b:2"], "node_"),
    self._tc_reg.get_completions("pt", "node_"))
