# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
self.assertEqual(0, len(debugger_cli_common.RichLine()))
self.assertEqual(0, len(debugger_cli_common.RichLine("")))
self.assertEqual(1, len(debugger_cli_common.RichLine("x")))
self.assertEqual(6, len(debugger_cli_common.RichLine("x y z ", "blue")))
