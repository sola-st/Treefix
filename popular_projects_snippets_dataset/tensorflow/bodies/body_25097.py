# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_widgets_test.py
nav_history = CNH(3)
nav_history.add_item("foo", RTL(["foo_out", "more_foo_out"]), 0)
nav_history.add_item("bar", RTL(["bar_out", "more_bar_out"]), 0)
nav_history.add_item("baz", RTL(["baz_out", "more_baz_out"]), 0)

nav_history.go_back()
nav_history.go_back()

output = nav_history.render(
    40,
    "prev",
    "next",
    latest_command_attribute="green",
    old_command_attribute="yellow")
self.assertEqual(1, len(output.lines))
self.assertEqual(
    "| " + CNH.BACK_ARROW_TEXT + " " + CNH.FORWARD_ARROW_TEXT +
    " | (-2) foo",
    output.lines[0])
self.assertEqual(6, output.font_attr_segs[0][0][0])
self.assertEqual(9, output.font_attr_segs[0][0][1])
self.assertEqual("next", output.font_attr_segs[0][0][2].content)

self.assertEqual(12, output.font_attr_segs[0][1][0])
self.assertEqual(17, output.font_attr_segs[0][1][1])
self.assertEqual("yellow", output.font_attr_segs[0][1][2])

self.assertEqual(17, output.font_attr_segs[0][2][0])
self.assertEqual(20, output.font_attr_segs[0][2][1])
self.assertEqual("yellow", output.font_attr_segs[0][2][2])
