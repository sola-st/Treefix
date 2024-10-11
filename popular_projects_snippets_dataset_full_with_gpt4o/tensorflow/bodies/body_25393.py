# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    80,
    command_sequence=[
        string_to_codes("babble -n 2 >\n"),
        self._EXIT
    ])

ui.register_command_handler("babble", self._babble, "")
ui.run_ui()

self.assertEqual(["ERROR: Redirect file path is empty"], ui.toasts)
self.assertEqual(0, len(ui.unwrapped_outputs))
