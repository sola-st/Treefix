# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    80,
    command_sequence=[
        string_to_codes("babble -n 1\n"),
        string_to_codes("babble -n 10\n"),
        string_to_codes("help\n"),
        string_to_codes("b") + [curses.KEY_UP],  # Navigate with prefix.
        string_to_codes("\n"),
        self._EXIT
    ])

ui.register_command_handler(
    "babble", self._babble, "babble some", prefix_aliases=["b"])
ui.run_ui()

self.assertEqual(["bar"], ui.unwrapped_outputs[0].lines)
self.assertEqual(["bar"] * 10, ui.unwrapped_outputs[1].lines)
self.assertEqual(["babble", "  Aliases: b", "", "  babble some"],
                 ui.unwrapped_outputs[2].lines[:4])
self.assertEqual(["bar"] * 10, ui.unwrapped_outputs[3].lines)
