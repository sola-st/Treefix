# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
registry = debugger_cli_common.CommandHandlerRegistry()

# Attempt to register an empty-string as a command prefix should trigger
# an exception.
with self.assertRaisesRegex(ValueError, "Empty command prefix"):
    registry.register_command_handler("", self._noop_handler, "")
