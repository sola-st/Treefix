# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    80,
    command_sequence=[
        string_to_codes("babble -n 1\t"),  # Trigger tab completion.
        string_to_codes("2\t"),  # With more prefix, tab again.
        string_to_codes("3\n"),
        self._EXIT
    ])

ui.register_command_handler(
    "babble", self._babble, "babble some", prefix_aliases=["b"])
ui.register_tab_comp_context(["babble", "b"], ["10", "120", "123"])
ui.run_ui()

# There should have been two different lists of candidates.
self.assertEqual([["10", "120", "123"], ["120", "123"]],
                 ui.candidates_lists)

self.assertEqual(1, len(ui.unwrapped_outputs))
self.assertEqual(1, len(ui.wrapped_outputs))
self.assertEqual(1, len(ui.scroll_messages))
self.assertEqual(["bar"] * 123, ui.unwrapped_outputs[0].lines)
self.assertEqual(["bar"] * 123, ui.wrapped_outputs[0].lines[:123])
