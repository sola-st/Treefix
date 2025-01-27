# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
registry = debugger_cli_common.CommandHandlerRegistry()
registry.register_command_handler(
    "noop",
    self._noop_handler,
    "No operation.\nI.e., do nothing.",
    prefix_aliases=["n", "NOOP"])
registry.register_command_handler(
    "cols",
    self._echo_screen_cols,
    "Show screen width in number of columns.",
    prefix_aliases=["c"])

help_lines = registry.get_help().lines

# The help info should list commands in alphabetically sorted order,
# regardless of order in which the commands are registered.
self.assertEqual("cols", help_lines[0])
self.assertTrue(help_lines[1].endswith("Aliases: c"))
self.assertFalse(help_lines[2])
self.assertTrue(help_lines[3].endswith(
    "Show screen width in number of columns."))

self.assertFalse(help_lines[4])
self.assertFalse(help_lines[5])

# The default help command should appear in the help output.
self.assertEqual("help", help_lines[6])

self.assertEqual("noop", help_lines[12])
self.assertTrue(help_lines[13].endswith("Aliases: n, NOOP"))
self.assertFalse(help_lines[14])
self.assertTrue(help_lines[15].endswith("No operation."))
self.assertTrue(help_lines[16].endswith("I.e., do nothing."))
