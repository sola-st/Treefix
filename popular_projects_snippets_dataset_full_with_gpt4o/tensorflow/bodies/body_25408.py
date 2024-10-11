# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
scroll_bar = curses_ui.ScrollBar(0, 0, 1, 7, 0, 0)
layout = scroll_bar.layout()
self.assertEqual(["  "] * 8, layout.lines)
self.assertEqual({}, layout.font_attr_segs)
