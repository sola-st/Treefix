# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
"""Test scrolling to specified (valid) indices in a tensor."""

ui = MockCursesUI(
    8,  # Use a small screen height to cause scrolling.
    80,
    command_sequence=[
        string_to_codes("print_ones --size 5\n"),
        string_to_codes("@[0, 0]\n"),  # Scroll to element [0, 0].
        string_to_codes("@1,0\n"),  # Scroll to element [3, 0].
        string_to_codes("@[0,2]\n"),  # Scroll back to line 0.
        self._EXIT
    ])

ui.register_command_handler("print_ones", self._print_ones,
                            "print an all-one matrix of specified size")
ui.run_ui()

self.assertEqual(4, len(ui.unwrapped_outputs))
self.assertEqual(4, len(ui.output_array_pointer_indices))

for i in range(4):
    cli_test_utils.assert_lines_equal_ignoring_whitespace(
        self, ["Tensor \"m\":", ""], ui.unwrapped_outputs[i].lines[:2])
    self.assertEqual(
        repr(np.ones([5, 5])).split("\n"), ui.unwrapped_outputs[i].lines[2:])

self.assertEqual({
    0: None,
    -1: [0, 0]
}, ui.output_array_pointer_indices[0])
self.assertEqual({
    0: [0, 0],
    -1: [2, 0]
}, ui.output_array_pointer_indices[1])
self.assertEqual({
    0: [1, 0],
    -1: [3, 0]
}, ui.output_array_pointer_indices[2])
self.assertEqual({
    0: [0, 0],
    -1: [2, 0]
}, ui.output_array_pointer_indices[3])
