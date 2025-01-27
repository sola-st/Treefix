# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Prepend (i.e., add to the front) a single line of text.

    Args:
      line: (str) The text to be added to the front.
      font_attr_segs: (list of tuples) Font attribute segments of the appended
        line.
    """

other = RichTextLines(line)
if font_attr_segs:
    other.font_attr_segs[0] = font_attr_segs
self._extend_before(other)
