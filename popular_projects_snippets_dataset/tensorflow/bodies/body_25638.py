# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
registry = debugger_cli_common.CommandHandlerRegistry()
registry.register_command_handler("raise_exception",
                                  self._handler_raising_exception, "")

# The registry should catch and wrap exceptions that occur during command
# handling.
cmd_output = registry.dispatch_command("raise_exception", [])
# The error output contains a stack trace.
# So the line count should be >= 2.
self.assertGreater(len(cmd_output.lines), 2)
self.assertTrue(cmd_output.lines[0].startswith(
    "Error occurred during handling of command"))
self.assertTrue(cmd_output.lines[1].endswith(self._intentional_error_msg))
