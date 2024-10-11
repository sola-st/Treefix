# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
with self.assertRaisesRegex(
    TypeError, "Attempt to enter non-str entry to command history"):
    self._cmd_hist.add_command(["print_tensor node_a:0"])
