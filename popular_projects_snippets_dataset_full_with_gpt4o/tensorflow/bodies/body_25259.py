# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Append a single line of text.

    Args:
      line: (str) The text to be added to the end.
      font_attr_segs: (list of tuples) Font attribute segments of the appended
        line.
    """

self._lines.append(line)
if font_attr_segs:
    self._font_attr_segs[len(self._lines) - 1] = font_attr_segs
