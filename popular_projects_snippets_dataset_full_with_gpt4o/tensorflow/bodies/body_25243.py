# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
output = self._registry.dispatch_command("pt",
                                         ["while/Identity:0", "-n", "10"])

self.assertEqual([
    "ERROR: Specified number (10) exceeds the number of available dumps "
    "(10) for tensor while/Identity:0"
], output.lines)
