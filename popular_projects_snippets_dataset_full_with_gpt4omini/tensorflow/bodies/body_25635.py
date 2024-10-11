# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
registry = debugger_cli_common.CommandHandlerRegistry()
registry.register_command_handler("wrong_return",
                                  self._handler_returning_wrong_type, "")

# If the command handler fails to return a RichTextLines instance, an error
# should be triggered.
with self.assertRaisesRegex(
    ValueError,
    "Return value from command handler.*is not None or a RichTextLines "
    "instance"):
    registry.dispatch_command("wrong_return", [])
