# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
"""Test that exit exception is correctly raised."""

registry = debugger_cli_common.CommandHandlerRegistry()
registry.register_command_handler("exit", self._exiting_handler, "")

self.assertTrue(registry.is_registered("exit"))

exit_token = None
try:
    registry.dispatch_command("exit", ["foo"])
except debugger_cli_common.CommandLineExit as e:
    exit_token = e.exit_token

self.assertEqual("foo", exit_token)
