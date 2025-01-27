# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/generate_examples_report.py
"""Produce a cell with the condition string `x`."""
s = html.escape(repr(x), quote=True)
color = "#44ff44" if x == SUCCESS else (
    "#ff4444" if x == FAILED else "#eeeeee")
handler = "ShowLog(%d, %d)" % (row, col)
fp.write("<td style='background-color: %s' onclick='%s'>%s</td>\n" % (
    color, handler, s))
