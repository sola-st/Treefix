# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
out = self._registry.dispatch_command("list_tensors", ["--bar"])
check_syntax_error_output(self, out, "list_tensors")
