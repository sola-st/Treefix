# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
self._cmd_hist.add_command("help 1")
self._cmd_hist.add_command("help 2")
self._cmd_hist.add_command("help 3")
self._cmd_hist.add_command("help 4")

cmd_hist_2 = debugger_cli_common.CommandHistory(
    limit=3, history_file_path=self._history_file_path)
self.assertEqual(["help 2", "help 3", "help 4"],
                 cmd_hist_2.most_recent_n(3))

with open(self._history_file_path, "rt") as f:
    self.assertEqual(
        ["help 2\n", "help 3\n", "help 4\n"], f.readlines())
