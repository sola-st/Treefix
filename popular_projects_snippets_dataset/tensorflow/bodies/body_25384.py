# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    6,  # Use a narrow window to trigger line wrapping
    command_sequence=[
        string_to_codes("babble -n 3 -l foo-bar-baz-qux\n"),
        string_to_codes("/foo\n"),  # Regex search and highlight.
        string_to_codes("/\n"),  # Continue scrolling down: 1st time.
        string_to_codes("/\n"),  # Continue scrolling down: 2nd time.
        string_to_codes("/\n"),  # Continue scrolling down: 3rd time.
        string_to_codes("/\n"),  # Continue scrolling down: 4th time.
        self._EXIT
    ])

ui.register_command_handler(
    "babble", self._babble, "babble some")
ui.run_ui()

self.assertEqual(4, len(ui.wrapped_outputs))
for wrapped_output in ui.wrapped_outputs:
    self.assertEqual(["foo-", "bar-", "baz-", "qux"] * 3,
                     wrapped_output.lines[0 : 12])

# The scroll location should reflect the line wrapping.
self.assertEqual([0, 0, 4, 8], ui.output_pad_rows)
