# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/readline_ui_test.py
"""Run UI with an initial command specified."""

ui = MockReadlineUI(command_sequence=["exit"])

ui.register_command_handler("babble", self._babble, "")
ui.run_ui(init_command="babble")

screen_outputs = ui.observers["screen_outputs"]
self.assertEqual(1, len(screen_outputs))
self.assertEqual(["bar"] * 60, screen_outputs[0].lines)
