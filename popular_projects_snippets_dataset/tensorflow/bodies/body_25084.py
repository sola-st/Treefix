# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/readline_ui_test.py
_, output_path = tempfile.mkstemp()  # safe to ignore fd

ui = MockReadlineUI(
    command_sequence=["babble -n 2 > %s" % output_path, "exit"])

ui.register_command_handler("babble", self._babble, "")
ui.run_ui()

screen_outputs = ui.observers["screen_outputs"]
self.assertEqual(1, len(screen_outputs))
self.assertEqual(["bar"] * 2, screen_outputs[0].lines)

with gfile.Open(output_path, "r") as f:
    self.assertEqual("bar\nbar\n", f.read())
