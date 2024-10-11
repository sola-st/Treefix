# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
# The returned completions should have sorted order.
self.assertEqual(
    (["node_a:1", "node_a:2", "node_b:1", "node_b:2"], "node_"),
    self._tc_reg.get_completions("print_tensor", "node_"))

self.assertEqual((["node_a:1", "node_a:2", "node_b:1", "node_b:2"],
                  "node_"), self._tc_reg.get_completions("pt", ""))

self.assertEqual((["node_a:1", "node_a:2"], "node_a:"),
                 self._tc_reg.get_completions("print_tensor", "node_a"))

self.assertEqual((["node_a:1"], "node_a:1"),
                 self._tc_reg.get_completions("pt", "node_a:1"))

self.assertEqual(([], ""),
                 self._tc_reg.get_completions("print_tensor", "node_a:3"))

self.assertEqual((None, None), self._tc_reg.get_completions("foo", "node_"))
