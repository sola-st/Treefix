# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
out = self._registry.dispatch_command("lt", ["-s", "foobar"])
self.assertIn("ValueError: Unsupported key to sort tensors by: foobar",
              out.lines)
