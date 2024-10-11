# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
"""Test regex search commands are recorded in command history."""

ui = MockCursesUI(
    40,
    80,
    command_sequence=[
        string_to_codes("babble -n 3\n"),
        string_to_codes("/(b|r)\n"),  # Regex search and highlight.
        string_to_codes("babble -n 4\n"),
        [curses.KEY_UP],
        [curses.KEY_UP],
        string_to_codes("\n"),  # Hit Up twice and Enter.
        self._EXIT
    ])

ui.register_command_handler(
    "babble", self._babble, "babble some", prefix_aliases=["b"])
ui.run_ui()

self.assertEqual(4, len(ui.wrapped_outputs))

self.assertEqual(["bar"] * 3, ui.wrapped_outputs[0].lines[:3])
self.assertEqual({}, ui.wrapped_outputs[0].font_attr_segs)

self.assertEqual(["bar"] * 3, ui.wrapped_outputs[1].lines[:3])
for i in range(3):
    self.assertEqual([(0, 1, "black_on_white"), (2, 3, "black_on_white")],
                     ui.wrapped_outputs[1].font_attr_segs[i])

self.assertEqual(["bar"] * 4, ui.wrapped_outputs[2].lines[:4])
self.assertEqual({}, ui.wrapped_outputs[2].font_attr_segs)

# The regex search command loaded from history should have worked on the
# new screen output.
self.assertEqual(["bar"] * 4, ui.wrapped_outputs[3].lines[:4])
for i in range(4):
    self.assertEqual([(0, 1, "black_on_white"), (2, 3, "black_on_white")],
                     ui.wrapped_outputs[3].font_attr_segs[i])
