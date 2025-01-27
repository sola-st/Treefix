# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    80,
    command_sequence=[string_to_codes("c\t"),  # Trigger tab completion.
                      string_to_codes("\n"),
                      self._EXIT])

ui.register_command_handler(
    "babble", self._babble, "babble some", prefix_aliases=["a"])
ui.run_ui()

# Only the invalid command "c" should have been issued.
self.assertEqual(1, len(ui.unwrapped_outputs))
self.assertEqual(1, len(ui.wrapped_outputs))
self.assertEqual(1, len(ui.scroll_messages))

self.assertEqual(["ERROR: Invalid command prefix \"c\""],
                 ui.unwrapped_outputs[0].lines)
self.assertEqual(["ERROR: Invalid command prefix \"c\""],
                 ui.wrapped_outputs[0].lines[:1])
