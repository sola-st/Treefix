# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
# Type "b" and trigger tab completion.
ui = MockCursesUI(
    40,
    80,
    command_sequence=[string_to_codes("b\t"), string_to_codes("\n"),
                      self._EXIT])

ui.register_command_handler(
    "babble", self._babble, "babble some", prefix_aliases=["ba"])
ui.run_ui()

# The automatically registered exit commands "exit" and "quit" should not
# appear in the tab completion candidates because they don't start with
# "b".
self.assertEqual([["ba", "babble"]], ui.candidates_lists)

# "ba" is a common prefix of the two candidates. So the "ba" command should
# have been issued after the Enter.
self.assertEqual(1, len(ui.unwrapped_outputs))
self.assertEqual(1, len(ui.wrapped_outputs))
self.assertEqual(1, len(ui.scroll_messages))
self.assertEqual(["bar"] * 60, ui.unwrapped_outputs[0].lines)
self.assertEqual(["bar"] * 60, ui.wrapped_outputs[0].lines[:60])
