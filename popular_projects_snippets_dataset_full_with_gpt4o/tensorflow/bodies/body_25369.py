# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    80,
    command_sequence=[string_to_codes("help\n"), self._EXIT])

help_intro = debugger_cli_common.RichTextLines(
    ["This is a curses UI.", "All it can do is 'babble'.", ""])
ui.register_command_handler(
    "babble", self._babble, "babble some", prefix_aliases=["b"])
ui.set_help_intro(help_intro)
ui.run_ui()

self.assertEqual(1, len(ui.unwrapped_outputs))
self.assertEqual(
    help_intro.lines + ["babble", "  Aliases: b", "", "  babble some"],
    ui.unwrapped_outputs[0].lines[:7])
