# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
"""Test continuing scrolling down to next regex match."""

ui = MockCursesUI(
    40,
    80,
    command_sequence=[
        string_to_codes("babble -n 3\n"),
        string_to_codes("/(b|r)\n"),  # Regex search and highlight.
        string_to_codes("/\n"),  # Continue scrolling down: 1st time.
        string_to_codes("/\n"),  # Continue scrolling down: 2nd time.
        string_to_codes("/\n"),  # Continue scrolling down: 3rd time.
        string_to_codes("/\n"),  # Continue scrolling down: 4th time.
        self._EXIT
    ])

ui.register_command_handler(
    "babble", self._babble, "babble some", prefix_aliases=["b"])
ui.run_ui()

# The 1st output is for the non-searched output. The other three are for
# the searched output. Even though continuation search "/" is performed
# four times, there should be only three searched outputs, because the
# last one has exceeded the end.
self.assertEqual(4, len(ui.unwrapped_outputs))

for i in range(4):
    self.assertEqual(["bar"] * 3, ui.unwrapped_outputs[i].lines)
    self.assertEqual({}, ui.unwrapped_outputs[i].font_attr_segs)

self.assertEqual(["bar"] * 3, ui.wrapped_outputs[0].lines[:3])
self.assertEqual({}, ui.wrapped_outputs[0].font_attr_segs)

for j in range(1, 4):
    self.assertEqual(["bar"] * 3, ui.wrapped_outputs[j].lines[:3])
    self.assertEqual({
        0: [(0, 1, "black_on_white"), (2, 3, "black_on_white")],
        1: [(0, 1, "black_on_white"), (2, 3, "black_on_white")],
        2: [(0, 1, "black_on_white"), (2, 3, "black_on_white")]
    }, ui.wrapped_outputs[j].font_attr_segs)

self.assertEqual([0, 0, 1, 2], ui.output_pad_rows)
