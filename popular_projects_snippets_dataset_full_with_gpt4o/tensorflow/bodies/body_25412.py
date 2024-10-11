# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
scroll_bar = curses_ui.ScrollBar(0, 0, 0, 7, 0, 20)
layout = scroll_bar.layout()
self.assertEqual(["U"] + [" "] * 6 + ["D"], layout.lines)
self.assertEqual(
    {0: [(0, 1, curses_ui.ScrollBar.BASE_ATTR)],
     1: [(0, 1, curses_ui.ScrollBar.BASE_ATTR)],
     7: [(0, 1, curses_ui.ScrollBar.BASE_ATTR)]},
    layout.font_attr_segs)
