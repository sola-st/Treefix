# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
scroll_bar = curses_ui.ScrollBar(0, 5, 1, 12, 10, 20)
self.assertIsNone(scroll_bar.get_click_command(0))
self.assertIsNone(scroll_bar.get_click_command(4))
self.assertEqual(curses_ui._SCROLL_UP_A_LINE,
                 scroll_bar.get_click_command(5))
self.assertEqual(curses_ui._SCROLL_UP,
                 scroll_bar.get_click_command(6))
self.assertEqual(curses_ui._SCROLL_UP,
                 scroll_bar.get_click_command(7))
self.assertIsNone(scroll_bar.get_click_command(8))
self.assertEqual(curses_ui._SCROLL_DOWN,
                 scroll_bar.get_click_command(10))
self.assertEqual(curses_ui._SCROLL_DOWN,
                 scroll_bar.get_click_command(11))
self.assertEqual(curses_ui._SCROLL_DOWN_A_LINE,
                 scroll_bar.get_click_command(12))
self.assertIsNone(scroll_bar.get_click_command(13))
