# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
registry = debugger_cli_common.CommandHandlerRegistry()

# Register and invoke a command handler that uses screen_info.
registry.register_command_handler("cols", self._echo_screen_cols, "")

cmd_output = registry.dispatch_command(
    "cols", [], screen_info={"cols": 100})
self.assertEqual(["cols = 100"], cmd_output.lines)
