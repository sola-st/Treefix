# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
self._cmd_hist.add_command("help")
self._cmd_hist.add_command("help")

self.assertEqual(["help"], self._cmd_hist.most_recent_n(2))
