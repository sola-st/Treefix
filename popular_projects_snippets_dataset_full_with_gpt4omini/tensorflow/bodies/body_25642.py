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

# Get help info for one of the two commands, using full prefix.
help_lines = registry.get_help("cols").lines

self.assertTrue(help_lines[0].endswith("cols"))
self.assertTrue(help_lines[1].endswith("Aliases: c"))
self.assertFalse(help_lines[2])
self.assertTrue(help_lines[3].endswith(
    "Show screen width in number of columns."))

# Get help info for one of the two commands, using alias.
help_lines = registry.get_help("c").lines

self.assertTrue(help_lines[0].endswith("cols"))
self.assertTrue(help_lines[1].endswith("Aliases: c"))
self.assertFalse(help_lines[2])
self.assertTrue(help_lines[3].endswith(
    "Show screen width in number of columns."))

# Get help info for a nonexistent command.
help_lines = registry.get_help("foo").lines

self.assertEqual("Invalid command prefix: \"foo\"", help_lines[0])
