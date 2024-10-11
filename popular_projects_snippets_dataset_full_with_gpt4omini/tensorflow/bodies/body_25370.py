# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    80,
    command_sequence=[string_to_codes("help\n"),
                      [curses.KEY_UP],  # Hit Up and Enter.
                      string_to_codes("\n"),
                      self._EXIT])

ui.register_command_handler(
    "babble", self._babble, "babble some", prefix_aliases=["b"])
ui.run_ui()

self.assertEqual(2, len(ui.unwrapped_outputs))

for i in [0, 1]:
    self.assertEqual(["babble", "  Aliases: b", "", "  babble some"],
                     ui.unwrapped_outputs[i].lines[:4])
