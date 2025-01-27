# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    80,
    command_sequence=[
        string_to_codes("babble -n 10 -k\n"),
        # A click off a hyperlink (too much to the right).
        [curses.KEY_MOUSE, 8, 4],
        self._EXIT
    ])
ui.register_command_handler("babble", self._babble, "")
ui.run_ui()

# The mouse click event should not triggered no command.
self.assertEqual(1, len(ui.unwrapped_outputs))
self.assertEqual(["bar"] * 10, ui.unwrapped_outputs[0].lines)

# This command should have generated no main menus.
self.assertEqual([None], ui.main_menu_list)
