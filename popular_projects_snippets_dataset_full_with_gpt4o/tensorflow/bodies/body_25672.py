# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
self.assertEqual([], self._cmd_hist.most_recent_n(3))

self._cmd_hist.add_command("list_tensors")
self._cmd_hist.add_command("node_info node_a")

self.assertEqual(["node_info node_a"], self._cmd_hist.most_recent_n(1))
self.assertEqual(["list_tensors", "node_info node_a"],
                 self._cmd_hist.most_recent_n(2))
self.assertEqual(["list_tensors", "node_info node_a"],
                 self._cmd_hist.most_recent_n(3))

self._cmd_hist.add_command("node_info node_b")

self.assertEqual(["node_info node_b"], self._cmd_hist.most_recent_n(1))
self.assertEqual(["node_info node_a", "node_info node_b"],
                 self._cmd_hist.most_recent_n(2))
self.assertEqual(["list_tensors", "node_info node_a", "node_info node_b"],
                 self._cmd_hist.most_recent_n(3))
self.assertEqual(["list_tensors", "node_info node_a", "node_info node_b"],
                 self._cmd_hist.most_recent_n(4))

# Go over the limit.
self._cmd_hist.add_command("node_info node_a")

self.assertEqual(["node_info node_a"], self._cmd_hist.most_recent_n(1))
self.assertEqual(["node_info node_b", "node_info node_a"],
                 self._cmd_hist.most_recent_n(2))
self.assertEqual(
    ["node_info node_a", "node_info node_b", "node_info node_a"],
    self._cmd_hist.most_recent_n(3))
self.assertEqual(
    ["node_info node_a", "node_info node_b", "node_info node_a"],
    self._cmd_hist.most_recent_n(4))
