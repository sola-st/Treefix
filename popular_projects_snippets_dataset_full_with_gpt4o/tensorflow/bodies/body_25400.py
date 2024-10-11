# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
ui = MockCursesUI(
    40,
    80,
    command_sequence=[
        string_to_codes("babble -n 10 -m\n"),
        # A click on the enabled menu item.
        [curses.KEY_MOUSE, 3, 2],
        self._EXIT
    ])
ui.register_command_handler("babble", self._babble, "")
ui.run_ui()

self.assertEqual(2, len(ui.unwrapped_outputs))
self.assertEqual(["bar"] * 10, ui.unwrapped_outputs[0].lines)
self.assertEqual(["bar"] * 60, ui.unwrapped_outputs[1].lines)

# Check the content of the menu.
self.assertEqual(["| babble again | ahoy | "], ui.main_menu_list[0].lines)
self.assertEqual(1, len(ui.main_menu_list[0].font_attr_segs))
self.assertEqual(1, len(ui.main_menu_list[0].font_attr_segs[0]))

item_annot = ui.main_menu_list[0].font_attr_segs[0][0]
self.assertEqual(2, item_annot[0])
self.assertEqual(14, item_annot[1])
self.assertEqual("babble", item_annot[2][0].content)
self.assertEqual("underline", item_annot[2][1])

# The output from the menu-triggered command does not have a menu.
self.assertIsNone(ui.main_menu_list[1])
