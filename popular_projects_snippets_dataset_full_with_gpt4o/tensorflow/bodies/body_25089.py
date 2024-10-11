# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_widgets_test.py
nav_history = CNH(10)
nav_history.add_item("foo", RTL(["bar"]), 0)

self.assertEqual(1, nav_history.size())
self.assertEqual(0, nav_history.pointer())

self.assertFalse(nav_history.can_go_forward())
self.assertFalse(nav_history.can_go_back())

output = nav_history.go_back()
self.assertEqual("foo", output.command)
self.assertEqual(["bar"], output.screen_output.lines)
self.assertEqual(0, output.scroll_position)
