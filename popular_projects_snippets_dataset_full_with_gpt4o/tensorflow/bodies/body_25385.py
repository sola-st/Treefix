# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
"""Test continuing scrolling when there is no regex match."""

ui = MockCursesUI(
    40,
    80,
    command_sequence=[
        string_to_codes("babble -n 3\n"),
        string_to_codes("/foo\n"),  # Regex search and highlight.
        string_to_codes("/\n"),  # Continue scrolling down.
        self._EXIT
    ])

ui.register_command_handler(
    "babble", self._babble, "babble some", prefix_aliases=["b"])
ui.run_ui()

# The regex search and continuation search in the 3rd command should not
# have produced any output.
self.assertEqual(1, len(ui.unwrapped_outputs))
self.assertEqual([0], ui.output_pad_rows)
