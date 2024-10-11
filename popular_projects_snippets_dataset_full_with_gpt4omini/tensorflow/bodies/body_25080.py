# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/readline_ui_test.py
"""Run UI with an initial command specified."""

ui = MockReadlineUI(command_sequence=["babble -n 3", "babble -n 6", "exit"])
ui.register_command_handler("babble", self._babble, "")
ui.run_ui()

screen_outputs = ui.observers["screen_outputs"]
self.assertEqual(2, len(screen_outputs))
self.assertEqual(["bar"] * 3, screen_outputs[0].lines)
self.assertEqual(["bar"] * 6, screen_outputs[1].lines)
