# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_widgets_test.py
nav_history = CNH(10)
self.assertEqual(0, nav_history.size())
self.assertFalse(nav_history.can_go_forward())
self.assertFalse(nav_history.can_go_back())

with self.assertRaisesRegex(ValueError, "Empty navigation history"):
    nav_history.go_back()
with self.assertRaisesRegex(ValueError, "Empty navigation history"):
    nav_history.go_forward()
with self.assertRaisesRegex(ValueError, "Empty navigation history"):
    nav_history.update_scroll_position(3)
