# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    80,
    command_sequence=[
        string_to_codes("babble -n 2\n"),
        [curses.KEY_NPAGE],   # Scroll down one line.
        string_to_codes("babble -n 4\n"),
        # A click on the back (prev) button of the nav bar.
        [curses.KEY_MOUSE, 3, 1],
        # A click on the forward (prev) button of the nav bar.
        [curses.KEY_MOUSE, 7, 1],
        self._EXIT
    ])
ui.register_command_handler("babble", self._babble, "")
ui.run_ui()

self.assertEqual(6, len(ui.unwrapped_outputs))
self.assertEqual(["bar"] * 2, ui.unwrapped_outputs[0].lines)
# From manual scroll.
self.assertEqual(["bar"] * 2, ui.unwrapped_outputs[1].lines)
self.assertEqual(["bar"] * 4, ui.unwrapped_outputs[2].lines)
# From history navigation.
self.assertEqual(["bar"] * 2, ui.unwrapped_outputs[3].lines)
# From history navigation's auto-scroll to history scroll position.
self.assertEqual(["bar"] * 2, ui.unwrapped_outputs[4].lines)
self.assertEqual(["bar"] * 4, ui.unwrapped_outputs[5].lines)

self.assertEqual(6, len(ui.scroll_messages))
self.assertIn("Scroll (PgDn): 0.00%", ui.scroll_messages[0])
self.assertIn("Scroll (PgUp): 100.00%", ui.scroll_messages[1])
self.assertIn("Scroll (PgDn): 0.00%", ui.scroll_messages[2])
self.assertIn("Scroll (PgDn): 0.00%", ui.scroll_messages[3])
self.assertIn("Scroll (PgUp): 100.00%", ui.scroll_messages[4])
self.assertIn("Scroll (PgDn): 0.00%", ui.scroll_messages[5])
