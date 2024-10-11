# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
scroll_bar = curses_ui.ScrollBar(0, 0, 1, 7, 0, 1)
self.assertIsNone(scroll_bar.get_click_command(0))
self.assertIsNone(scroll_bar.get_click_command(3))
self.assertIsNone(scroll_bar.get_click_command(7))
self.assertIsNone(scroll_bar.get_click_command(8))
