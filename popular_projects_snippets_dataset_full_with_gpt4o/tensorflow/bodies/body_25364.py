# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
"""Scroll tall output with PageDown and PageUp."""

# Use PageDown and PageUp to scroll back and forth a little before exiting.
ui = MockCursesUI(
    40,
    80,
    command_sequence=[string_to_codes("babble\n"), [curses.KEY_NPAGE] * 2 +
                      [curses.KEY_PPAGE] + self._EXIT])

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
self.assertIn("Mouse:", ui.scroll_messages[0])

# After 1st scrolling (PageDown).
# The screen output shouldn't have changed. Only the viewport should.
self.assertEqual(["bar"] * 60, ui.unwrapped_outputs[0].lines)
self.assertEqual(["bar"] * 60, ui.wrapped_outputs[0].lines[:60])
self.assertIn("Scroll (PgDn/PgUp): 1.69%", ui.scroll_messages[1])
self.assertIn("Mouse:", ui.scroll_messages[1])

# After 2nd scrolling (PageDown).
self.assertIn("Scroll (PgDn/PgUp): 3.39%", ui.scroll_messages[2])
self.assertIn("Mouse:", ui.scroll_messages[2])

# After 3rd scrolling (PageUp).
self.assertIn("Scroll (PgDn/PgUp): 1.69%", ui.scroll_messages[3])
self.assertIn("Mouse:", ui.scroll_messages[3])
