# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common_test.py
registry = debugger_cli_common.CommandHandlerRegistry()
registry.register_command_handler(
    "noop",
    self._noop_handler,
    "No operation.\nI.e., do nothing.",
    prefix_aliases=["n", "NOOP"])

help_intro = debugger_cli_common.RichTextLines(
    ["Introductory comments.", ""])
registry.set_help_intro(help_intro)

output = registry.dispatch_command("help", [])
self.assertEqual(help_intro.lines + [
    "help", "  Aliases: h", "", "  Print this help message.", "", "",
    "noop", "  Aliases: n, NOOP", "", "  No operation.",
    "  I.e., do nothing.", "", "",
    "version", "  Aliases: ver", "",
    "  Print the versions of TensorFlow and its key dependencies.", "", ""
], output.lines)
