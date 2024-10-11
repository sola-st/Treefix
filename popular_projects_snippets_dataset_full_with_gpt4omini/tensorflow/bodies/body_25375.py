# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    80,
    command_sequence=[string_to_codes("babble\n"),
                      [curses.KEY_RESIZE, 100, 85],  # Resize to [100, 85]
                      self._EXIT])

ui.register_command_handler(
    "babble", self._babble, "babble some", prefix_aliases=["b"])
ui.run_ui()

# The resize event should have caused a second screen output event.
self.assertEqual(2, len(ui.unwrapped_outputs))
self.assertEqual(2, len(ui.wrapped_outputs))
self.assertEqual(2, len(ui.scroll_messages))

# The 1st and 2nd screen outputs should be identical (unwrapped).
self.assertEqual(ui.unwrapped_outputs[0], ui.unwrapped_outputs[1])

# The 1st scroll info should contain scrolling, because the screen size
# is less than the number of lines in the output.
self.assertIn("Scroll (PgDn): 0.00%", ui.scroll_messages[0])
