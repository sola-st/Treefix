# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
with self.assertRaisesRegex(ValueError, "Encountered negative index"):
    self._original.slice(0, -1)
