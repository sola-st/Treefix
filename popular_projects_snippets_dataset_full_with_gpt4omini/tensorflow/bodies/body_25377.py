# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    80,
    command_sequence=[string_to_codes("\t"),  # Trigger tab completion.
                      string_to_codes("\n"),
                      self._EXIT])

ui.register_command_handler(
    "babble", self._babble, "babble some", prefix_aliases=["a"])
# Use a different alias "a" instead.
ui.run_ui()

# The manually registered command, along with the automatically registered
# exit commands should appear in the candidates.
self.assertEqual(
    [["a", "babble", "cfg", "config", "exit", "h", "help", "m", "mouse",
      "quit"]], ui.candidates_lists)

# The two candidates have no common prefix. So no command should have been
# issued.
self.assertEqual(0, len(ui.unwrapped_outputs))
self.assertEqual(0, len(ui.wrapped_outputs))
self.assertEqual(0, len(ui.scroll_messages))
