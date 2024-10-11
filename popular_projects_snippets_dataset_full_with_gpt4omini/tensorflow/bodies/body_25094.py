# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_widgets_test.py
nav_history = CNH(2)

output = nav_history.render(40, "prev", "next")
self.assertEqual(1, len(output.lines))
self.assertEqual(
    "| " + CNH.BACK_ARROW_TEXT + " " + CNH.FORWARD_ARROW_TEXT,
    output.lines[0])
self.assertEqual({}, output.font_attr_segs)
