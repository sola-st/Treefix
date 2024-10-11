# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
registry = debugger_cli_common.CommandHandlerRegistry()
registry.register_command_handler("noop", self._noop_handler, "")

# Registering the same command prefix more than once should trigger an
# exception.
with self.assertRaisesRegex(
    ValueError, "A handler is already registered for command prefix"):
    registry.register_command_handler("noop", self._noop_handler, "")

cmd_output = registry.dispatch_command("noop", [])
self.assertEqual(["Done."], cmd_output.lines)
