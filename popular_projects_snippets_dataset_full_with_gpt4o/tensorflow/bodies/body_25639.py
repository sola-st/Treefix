# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
registry = debugger_cli_common.CommandHandlerRegistry()

# Attempt to register a non-callable handler should fail.
with self.assertRaisesRegex(ValueError, "handler is not callable"):
    registry.register_command_handler("non_callable", 1, "")
