# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
scroll_bar = curses_ui.ScrollBar(0, 0, 1, 7, 19, 20)
layout = scroll_bar.layout()
self.assertEqual(["UP"] + ["  "] * 6 + ["DN"], layout.lines)
self.assertEqual(
    {0: [(0, 2, curses_ui.ScrollBar.BASE_ATTR)],
     6: [(0, 2, curses_ui.ScrollBar.BASE_ATTR)],
     7: [(0, 2, curses_ui.ScrollBar.BASE_ATTR)]},
    layout.font_attr_segs)
