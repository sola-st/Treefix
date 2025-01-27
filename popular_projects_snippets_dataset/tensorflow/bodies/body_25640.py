# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
registry = debugger_cli_common.CommandHandlerRegistry()

with self.assertRaisesRegex(ValueError, "help_info is not a str"):
    registry.register_command_handler("noop", self._noop_handler, ["foo"])
