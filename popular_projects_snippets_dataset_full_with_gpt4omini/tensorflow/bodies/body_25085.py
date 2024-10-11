# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/readline_ui_test.py
"""Run UI with an initial command specified."""

ui = MockReadlineUI(command_sequence=[
    "config set graph_recursion_depth 5", "config show", "exit"])
ui.run_ui()
outputs = ui.observers["screen_outputs"]
self.assertEqual(
    ["Command-line configuration:",
     "",
     "  graph_recursion_depth: 5"], outputs[1].lines[:3])
