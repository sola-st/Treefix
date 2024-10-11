# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
"""Test regex search."""

ui = MockCursesUI(
    40,
    80,
    command_sequence=[
        string_to_codes("babble -n 3\n"),
        string_to_codes("/(b|r)\n"),  # Regex search and highlight.
        string_to_codes("/a\n"),  # Regex search and highlight.
        self._EXIT
    ])

ui.register_command_handler(
    "babble", self._babble, "babble some", prefix_aliases=["b"])
ui.run_ui()

# The unwrapped (original) output should never have any highlighting.
self.assertEqual(3, len(ui.unwrapped_outputs))
for i in range(3):
    self.assertEqual(["bar"] * 3, ui.unwrapped_outputs[i].lines)
    self.assertEqual({}, ui.unwrapped_outputs[i].font_attr_segs)

# The wrapped outputs should show highlighting depending on the regex.
self.assertEqual(3, len(ui.wrapped_outputs))

# The first output should have no highlighting.
self.assertEqual(["bar"] * 3, ui.wrapped_outputs[0].lines[:3])
self.assertEqual({}, ui.wrapped_outputs[0].font_attr_segs)

# The second output should have highlighting for "b" and "r".
self.assertEqual(["bar"] * 3, ui.wrapped_outputs[1].lines[:3])
for i in range(3):
    self.assertEqual([(0, 1, "black_on_white"), (2, 3, "black_on_white")],
                     ui.wrapped_outputs[1].font_attr_segs[i])

# The third output should have highlighting for "a" only.
self.assertEqual(["bar"] * 3, ui.wrapped_outputs[1].lines[:3])
for i in range(3):
    self.assertEqual([(1, 2, "black_on_white")],
                     ui.wrapped_outputs[2].font_attr_segs[i])
