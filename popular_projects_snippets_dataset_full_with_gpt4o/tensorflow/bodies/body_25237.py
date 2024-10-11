# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
out = self._registry.dispatch_command(
    "list_inputs", ["control_deps/z/foo"])

self.assertEqual([
    "ERROR: There is no node named \"control_deps/z/foo\" in the "
    "partition graphs"], out.lines)
