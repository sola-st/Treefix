# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
"""Handle an unregistered command prefix."""

ui = MockCursesUI(
    40,
    80,
    command_sequence=[string_to_codes("foo\n"), self._EXIT])
ui.run_ui()

# Screen output/scrolling should have happened exactly once.
self.assertEqual(1, len(ui.unwrapped_outputs))
self.assertEqual(1, len(ui.wrapped_outputs))
self.assertEqual(1, len(ui.scroll_messages))

self.assertEqual(["ERROR: Invalid command prefix \"foo\""],
                 ui.unwrapped_outputs[0].lines)
# TODO(cais): Add explanation for the 35 extra lines.
self.assertEqual(["ERROR: Invalid command prefix \"foo\""],
                 ui.wrapped_outputs[0].lines[:1])
# A single line of output should not have caused scrolling.
self.assertNotIn("Scroll", ui.scroll_messages[0])
self.assertIn("Mouse:", ui.scroll_messages[0])
