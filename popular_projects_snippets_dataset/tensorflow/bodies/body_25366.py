# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
"""Scroll tall output with PageDown and PageUp."""

# Use End and Home to scroll a little before exiting to test scrolling.
ui = MockCursesUI(
    40,
    80,
    command_sequence=[
        string_to_codes("babble\n"),
        [curses.KEY_END] * 2 + [curses.KEY_HOME] + self._EXIT
    ])

ui.register_command_handler("babble", self._babble, "")
ui.run_ui()

# Screen output/scrolling should have happened exactly once.
self.assertEqual(4, len(ui.unwrapped_outputs))
self.assertEqual(4, len(ui.wrapped_outputs))
self.assertEqual(4, len(ui.scroll_messages))

# Before scrolling.
self.assertEqual(["bar"] * 60, ui.unwrapped_outputs[0].lines)
self.assertEqual(["bar"] * 60, ui.wrapped_outputs[0].lines[:60])

# Initial scroll: At the top.
self.assertIn("Scroll (PgDn): 0.00%", ui.scroll_messages[0])

# After 1st scrolling (End).
self.assertIn("Scroll (PgUp): 100.00%", ui.scroll_messages[1])

# After 2nd scrolling (End).
self.assertIn("Scroll (PgUp): 100.00%", ui.scroll_messages[2])

# After 3rd scrolling (Hhome).
self.assertIn("Scroll (PgDn): 0.00%", ui.scroll_messages[3])
