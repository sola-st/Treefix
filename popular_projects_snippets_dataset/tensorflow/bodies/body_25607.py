# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
exit_exc = debugger_cli_common.CommandLineExit()

self.assertTrue(isinstance(exit_exc, Exception))
