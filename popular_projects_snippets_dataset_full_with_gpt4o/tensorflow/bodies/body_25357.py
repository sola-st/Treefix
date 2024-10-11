# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(40, 80)

self.assertEqual(0, ui._command_pointer)
self.assertEqual([], ui._active_command_history)
self.assertEqual("", ui._pending_command)
