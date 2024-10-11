# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
"""Test continuation scrolling when no regex search has been performed."""

ui = MockCursesUI(
    40,
    80,
    command_sequence=[
        string_to_codes("babble -n 3\n"),
        string_to_codes("/\n"),  # Continue scrolling without search first.
        self._EXIT
    ])

ui.register_command_handler(
    "babble", self._babble, "babble some", prefix_aliases=["b"])
ui.run_ui()

self.assertEqual(1, len(ui.unwrapped_outputs))
self.assertEqual([0], ui.output_pad_rows)
