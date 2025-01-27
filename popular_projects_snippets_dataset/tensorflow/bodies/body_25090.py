# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_widgets_test.py
nav_history = CNH(2)
nav_history.add_item("foo", RTL(["foo_output"]), 0)
nav_history.add_item("bar", RTL(["bar_output"]), 0)

self.assertEqual(2, nav_history.size())
self.assertEqual(1, nav_history.pointer())
self.assertTrue(nav_history.can_go_back())
self.assertFalse(nav_history.can_go_forward())

nav_history.add_item("baz", RTL(["baz_output"]), 0)

self.assertEqual(2, nav_history.size())
self.assertEqual(1, nav_history.pointer())
self.assertTrue(nav_history.can_go_back())
self.assertFalse(nav_history.can_go_forward())

item = nav_history.go_back()
self.assertEqual("bar", item.command)
self.assertFalse(nav_history.can_go_back())
self.assertTrue(nav_history.can_go_forward())

item = nav_history.go_forward()
self.assertEqual("baz", item.command)
self.assertTrue(nav_history.can_go_back())
self.assertFalse(nav_history.can_go_forward())
