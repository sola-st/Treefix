# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
registry = debugger_cli_common.CommandHandlerRegistry()
registry.register_command_handler(
    "noop", self._noop_handler, "", prefix_aliases=["n", "NOOP"])

# is_registered() should work for full prefix and aliases.
self.assertTrue(registry.is_registered("noop"))
self.assertTrue(registry.is_registered("n"))
self.assertTrue(registry.is_registered("NOOP"))

cmd_output = registry.dispatch_command("n", [])
self.assertEqual(["Done."], cmd_output.lines)

cmd_output = registry.dispatch_command("NOOP", [])
self.assertEqual(["Done."], cmd_output.lines)
