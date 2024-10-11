# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    80,
    command_sequence=[
        string_to_codes("babble -n 10 -m\n"),
        # A click on the disabled menu item.
        [curses.KEY_MOUSE, 18, 1],
        self._EXIT
    ])
ui.register_command_handler("babble", self._babble, "")
ui.run_ui()

self.assertEqual(1, len(ui.unwrapped_outputs))
self.assertEqual(["bar"] * 10, ui.unwrapped_outputs[0].lines)
