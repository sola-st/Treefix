# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
self._cmd_hist.add_command("node_info node_b")
self._cmd_hist.add_command("list_tensors")
self._cmd_hist.add_command("node_info node_a")

self.assertEqual(["node_info node_b", "node_info node_a"],
                 self._cmd_hist.lookup_prefix("node_info", 10))

self.assertEqual(["node_info node_a"], self._cmd_hist.lookup_prefix(
    "node_info", 1))

self.assertEqual([], self._cmd_hist.lookup_prefix("print_tensor", 10))
