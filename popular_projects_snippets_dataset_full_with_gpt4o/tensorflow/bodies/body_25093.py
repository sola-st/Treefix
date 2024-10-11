# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_widgets_test.py
nav_history = CNH(2)
nav_history.add_item("foo", RTL(["foo_out", "more_foo_out"]), 0)
nav_history.add_item("bar", RTL(["bar_out", "more_bar_out"]), 0)

item = nav_history.go_back()
self.assertEqual("foo", item.command)
self.assertEqual(0, item.scroll_position)

nav_history.update_scroll_position(1)
nav_history.go_forward()
item = nav_history.go_back()
self.assertEqual("foo", item.command)
self.assertEqual(1, item.scroll_position)

item = nav_history.go_forward()
self.assertEqual("bar", item.command)
self.assertEqual(0, item.scroll_position)
