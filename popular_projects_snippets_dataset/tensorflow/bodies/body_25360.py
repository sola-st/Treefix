# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
"""Make sure that the UI can exit properly after launch."""

ui = MockCursesUI(40, 80, command_sequence=[self._EXIT])
ui.run_ui()

# No screen output should have happened.
self.assertEqual(0, len(ui.unwrapped_outputs))
