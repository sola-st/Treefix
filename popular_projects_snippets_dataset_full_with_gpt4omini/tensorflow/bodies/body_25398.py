# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    80,
    command_sequence=[
        string_to_codes("babble -n 10 -k\n"),
        string_to_codes("foo"),  # Enter some existing code in the textbox.
        [curses.KEY_MOUSE, 1, 4],  # A click on a hyperlink.
        self._EXIT
    ])
ui.register_command_handler("babble", self._babble, "")
ui.run_ui()

self.assertEqual(2, len(ui.unwrapped_outputs))
self.assertEqual(["bar"] * 10, ui.unwrapped_outputs[0].lines)
self.assertEqual(["bar"] * 60, ui.unwrapped_outputs[1].lines)
