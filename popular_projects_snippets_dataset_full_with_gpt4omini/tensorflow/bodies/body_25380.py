# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    80,
    command_sequence=[
        string_to_codes("babble -n 3\t"),  # Trigger tab completion.
        string_to_codes("\n"),
        self._EXIT
    ])

ui.register_command_handler(
    "babble", self._babble, "babble some", prefix_aliases=["b"])
ui.register_tab_comp_context(["babble", "b"], ["10", "20", "30", "300"])
ui.run_ui()

self.assertEqual([["30", "300"]], ui.candidates_lists)

self.assertEqual(1, len(ui.unwrapped_outputs))
self.assertEqual(1, len(ui.wrapped_outputs))
self.assertEqual(1, len(ui.scroll_messages))
self.assertEqual(["bar"] * 30, ui.unwrapped_outputs[0].lines)
self.assertEqual(["bar"] * 30, ui.wrapped_outputs[0].lines[:30])
