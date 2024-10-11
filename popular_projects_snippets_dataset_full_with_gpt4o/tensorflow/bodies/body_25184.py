# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
"""Test attempt to use a nonexistent tensor filter."""

out = self._registry.dispatch_command("lt", ["-f", "foo_filter"])

self.assertEqual(["ERROR: There is no tensor filter named \"foo_filter\"."],
                 out.lines)
check_main_menu(self, out, list_tensors_enabled=False)
