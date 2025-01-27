# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
with self.assertRaisesRegex(ValueError, "Invalid regular expression"):
    debugger_cli_common.regex_find(self._orig_screen_output, "[", "yellow")
