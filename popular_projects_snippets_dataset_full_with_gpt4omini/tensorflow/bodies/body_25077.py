# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/readline_ui_test.py
"""Make sure that the UI can exit properly after launch."""

ui = MockReadlineUI(command_sequence=["exit"])
ui.run_ui()

# No screen output should have happened.
self.assertEqual(0, len(ui.observers["screen_outputs"]))
