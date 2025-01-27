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

# Get help for all commands.
output = registry.dispatch_command("help", [])
self.assertEqual(["cols", "  Aliases: c", "",
                  "  Show screen width in number of columns.", "", "",
                  "help", "  Aliases: h", "", "  Print this help message.",
                  "", "", "noop", "  Aliases: n, NOOP", "",
                  "  No operation.", "  I.e., do nothing.", "", "",
                  "version", "  Aliases: ver", "",
                  "  Print the versions of TensorFlow and its key "
                  "dependencies.", "", ""],
                 output.lines)

# Get help for one specific command prefix.
output = registry.dispatch_command("help", ["noop"])
self.assertEqual(["noop", "  Aliases: n, NOOP", "", "  No operation.",
                  "  I.e., do nothing."], output.lines)

# Get help for a nonexistent command prefix.
output = registry.dispatch_command("help", ["foo"])
self.assertEqual(["Invalid command prefix: \"foo\""], output.lines)
