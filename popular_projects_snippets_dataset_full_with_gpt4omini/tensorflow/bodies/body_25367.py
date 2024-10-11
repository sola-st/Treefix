# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
"""Run UI with an initial command specified."""

ui = MockCursesUI(40, 80, command_sequence=[self._EXIT])

ui.register_command_handler("babble", self._babble, "")
ui.run_ui(init_command="babble")

self.assertEqual(1, len(ui.unwrapped_outputs))

self.assertEqual(["bar"] * 60, ui.unwrapped_outputs[0].lines)
self.assertEqual(["bar"] * 60, ui.wrapped_outputs[0].lines[:60])
self.assertIn("Scroll (PgDn): 0.00%", ui.scroll_messages[0])
