# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    80,
    command_sequence=[
        string_to_codes("babble -n 2\n"),
        string_to_codes("babble -n 4\n"),
        string_to_codes("prev\n"),
        string_to_codes("next\n"),
        string_to_codes("next\n"),  # Navigate over latest limit.
        self._EXIT
    ])
ui.register_command_handler("babble", self._babble, "")
ui.run_ui()

self.assertEqual(4, len(ui.unwrapped_outputs))
self.assertEqual(["bar"] * 2, ui.unwrapped_outputs[0].lines)
self.assertEqual(["bar"] * 4, ui.unwrapped_outputs[1].lines)
self.assertEqual(["bar"] * 2, ui.unwrapped_outputs[2].lines)
self.assertEqual(["bar"] * 4, ui.unwrapped_outputs[3].lines)

self.assertEqual("At the LATEST in navigation history!", ui.toasts[-2])
