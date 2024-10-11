# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_widgets_test.py
nav_history = CNH(2)
nav_history.add_item("long_command", RTL(["output"]), 0)

output = nav_history.render(
    15,
    "prev",
    "next",
    latest_command_attribute="green",
    old_command_attribute="yellow")
self.assertEqual(1, len(output.lines))
self.assertEqual(
    "| " + CNH.BACK_ARROW_TEXT + " " + CNH.FORWARD_ARROW_TEXT +
    " | lon",
    output.lines[0])

self.assertEqual(12, output.font_attr_segs[0][0][0])
self.assertEqual(15, output.font_attr_segs[0][0][1])
self.assertEqual("green", output.font_attr_segs[0][0][2])
