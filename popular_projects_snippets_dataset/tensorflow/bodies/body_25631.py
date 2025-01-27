# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
registry = debugger_cli_common.CommandHandlerRegistry()
registry.register_command_handler("noop", self._noop_handler, "")

self.assertTrue(registry.is_registered("noop"))
self.assertFalse(registry.is_registered("beep"))

cmd_output = registry.dispatch_command("noop", [])
self.assertEqual(["Done."], cmd_output.lines)

# Attempt to invoke an unregistered command prefix should trigger an
# exception.
with self.assertRaisesRegex(ValueError, "No handler is registered"):
    registry.dispatch_command("beep", [])

# Empty command prefix should trigger an exception.
with self.assertRaisesRegex(ValueError, "Prefix is empty"):
    registry.dispatch_command("", [])
