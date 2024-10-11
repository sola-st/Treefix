# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/readline_ui_test.py
"""Issue an empty command then exit."""

ui = MockReadlineUI(command_sequence=["", "exit"])
ui.run_ui()
self.assertEqual(1, len(ui.observers["screen_outputs"]))
