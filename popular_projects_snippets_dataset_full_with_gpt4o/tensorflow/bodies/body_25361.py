# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
"""Issue an empty command then exit."""

ui = MockCursesUI(40, 80, command_sequence=[[], self._EXIT])
ui.run_ui()

# Empty command should not lead to any screen output.
self.assertEqual(0, len(ui.unwrapped_outputs))
