# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
"""Test scrolling to specified invalid indices in a tensor."""

ui = MockCursesUI(
    8,  # Use a small screen height to cause scrolling.
    80,
    command_sequence=[
        string_to_codes("print_ones --size 5\n"),
        string_to_codes("@[10, 0]\n"),  # Scroll to invalid indices.
        string_to_codes("@[]\n"),  # Scroll to invalid indices.
        string_to_codes("@\n"),  # Scroll to invalid indices.
        self._EXIT
    ])

ui.register_command_handler("print_ones", self._print_ones,
                            "print an all-one matrix of specified size")
ui.run_ui()

# Because all scroll-by-indices commands are invalid, there should be only
# one output event.
self.assertEqual(1, len(ui.unwrapped_outputs))
self.assertEqual(1, len(ui.output_array_pointer_indices))

# Check error messages.
self.assertEqual("ERROR: Indices exceed tensor dimensions.", ui.toasts[2])
self.assertEqual("ERROR: invalid literal for int() with base 10: ''",
                 ui.toasts[4])
self.assertEqual("ERROR: Empty indices.", ui.toasts[6])
