# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    80,
    command_sequence=[string_to_codes("b\t"),  # Trigger tab completion.
                      string_to_codes("\n"),
                      self._EXIT])

ui.register_command_handler(
    "babble", self._babble, "babble some", prefix_aliases=["a"])
ui.run_ui()

# There is only one candidate, so no candidates should have been displayed.
# Instead, the completion should have been automatically keyed in, leading
# to the "babble" command being issue.
self.assertEqual([[]], ui.candidates_lists)

self.assertEqual(1, len(ui.unwrapped_outputs))
self.assertEqual(1, len(ui.wrapped_outputs))
self.assertEqual(1, len(ui.scroll_messages))
self.assertEqual(["bar"] * 60, ui.unwrapped_outputs[0].lines)
self.assertEqual(["bar"] * 60, ui.wrapped_outputs[0].lines[:60])
