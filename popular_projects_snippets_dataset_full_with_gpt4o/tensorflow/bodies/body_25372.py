# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    80,
    command_sequence=[string_to_codes("help\n"),
                      string_to_codes("babble\n"),
                      [curses.KEY_UP],
                      [curses.KEY_UP],
                      [curses.KEY_UP],  # Hit Up three times and Enter.
                      string_to_codes("\n"),
                      self._EXIT])

ui.register_command_handler(
    "babble", self._babble, "babble some", prefix_aliases=["b"])
ui.run_ui()

self.assertEqual(3, len(ui.unwrapped_outputs))

# The 1st and 3rd outputs are for command "help".
for i in [0, 2]:
    self.assertEqual(["babble", "  Aliases: b", "", "  babble some"],
                     ui.unwrapped_outputs[i].lines[:4])

# The 2nd output is for command "babble".
self.assertEqual(["bar"] * 60, ui.unwrapped_outputs[1].lines)
