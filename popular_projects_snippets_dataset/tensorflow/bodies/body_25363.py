# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
"""Handle a command with invalid syntax."""

ui = MockCursesUI(
    40,
    80,
    command_sequence=[string_to_codes("babble -z\n"), self._EXIT])

ui.register_command_handler("babble", self._babble, "")
ui.run_ui()

# Screen output/scrolling should have happened exactly once.
self.assertEqual(1, len(ui.unwrapped_outputs))
self.assertEqual(1, len(ui.wrapped_outputs))
self.assertEqual(1, len(ui.scroll_messages))
self.assertIn("Mouse:", ui.scroll_messages[0])
self.assertEqual(
    ["Syntax error for command: babble", "For help, do \"help babble\""],
    ui.unwrapped_outputs[0].lines)
