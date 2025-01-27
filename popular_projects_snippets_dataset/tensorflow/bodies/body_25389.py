# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
"""Test displaying tensor with indices."""

ui = MockCursesUI(
    9,  # Use a small screen height to cause scrolling.
    80,
    command_sequence=[
        string_to_codes("print_ones --size 5\n"),
        [curses.KEY_NPAGE],
        [curses.KEY_NPAGE],
        [curses.KEY_NPAGE],
        [curses.KEY_END],
        [curses.KEY_NPAGE],  # This PageDown goes over the bottom limit.
        [curses.KEY_PPAGE],
        [curses.KEY_PPAGE],
        [curses.KEY_PPAGE],
        [curses.KEY_HOME],
        [curses.KEY_PPAGE],  # This PageDown goes over the top limit.
        self._EXIT
    ])

ui.register_command_handler("print_ones", self._print_ones,
                            "print an all-one matrix of specified size")
ui.run_ui()

self.assertEqual(11, len(ui.unwrapped_outputs))
self.assertEqual(11, len(ui.output_array_pointer_indices))
self.assertEqual(11, len(ui.scroll_messages))

for i in range(11):
    cli_test_utils.assert_lines_equal_ignoring_whitespace(
        self, ["Tensor \"m\":", ""], ui.unwrapped_outputs[i].lines[:2])
    self.assertEqual(
        repr(np.ones([5, 5])).split("\n"), ui.unwrapped_outputs[i].lines[2:])

self.assertEqual({
    0: None,
    -1: [1, 0]
}, ui.output_array_pointer_indices[0])
self.assertIn(" Scroll (PgDn): 0.00% -[1,0] ", ui.scroll_messages[0])

# Scrolled down one line.
self.assertEqual({
    0: None,
    -1: [2, 0]
}, ui.output_array_pointer_indices[1])
self.assertIn(" Scroll (PgDn/PgUp): 16.67% -[2,0] ", ui.scroll_messages[1])

# Scrolled down one line.
self.assertEqual({
    0: [0, 0],
    -1: [3, 0]
}, ui.output_array_pointer_indices[2])
self.assertIn(" Scroll (PgDn/PgUp): 33.33% [0,0]-[3,0] ",
              ui.scroll_messages[2])

# Scrolled down one line.
self.assertEqual({
    0: [1, 0],
    -1: [4, 0]
}, ui.output_array_pointer_indices[3])
self.assertIn(" Scroll (PgDn/PgUp): 50.00% [1,0]-[4,0] ",
              ui.scroll_messages[3])

# Scroll to the bottom.
self.assertEqual({
    0: [4, 0],
    -1: None
}, ui.output_array_pointer_indices[4])
self.assertIn(" Scroll (PgUp): 100.00% [4,0]- ", ui.scroll_messages[4])

# Attempt to scroll beyond the bottom should lead to no change.
self.assertEqual({
    0: [4, 0],
    -1: None
}, ui.output_array_pointer_indices[5])
self.assertIn(" Scroll (PgUp): 100.00% [4,0]- ", ui.scroll_messages[5])

# Scrolled up one line.
self.assertEqual({
    0: [3, 0],
    -1: None
}, ui.output_array_pointer_indices[6])
self.assertIn(" Scroll (PgDn/PgUp): 83.33% [3,0]- ", ui.scroll_messages[6])

# Scrolled up one line.
self.assertEqual({
    0: [2, 0],
    -1: None
}, ui.output_array_pointer_indices[7])
self.assertIn(" Scroll (PgDn/PgUp): 66.67% [2,0]- ", ui.scroll_messages[7])

# Scrolled up one line.
self.assertEqual({
    0: [1, 0],
    -1: [4, 0]
}, ui.output_array_pointer_indices[8])
self.assertIn(" Scroll (PgDn/PgUp): 50.00% [1,0]-[4,0] ",
              ui.scroll_messages[8])

# Scroll to the top.
self.assertEqual({
    0: None,
    -1: [1, 0]
}, ui.output_array_pointer_indices[9])
self.assertIn(" Scroll (PgDn): 0.00% -[1,0] ", ui.scroll_messages[9])

# Attempt to scroll pass the top limit should lead to no change.
self.assertEqual({
    0: None,
    -1: [1, 0]
}, ui.output_array_pointer_indices[10])
self.assertIn(" Scroll (PgDn): 0.00% -[1,0] ", ui.scroll_messages[10])
