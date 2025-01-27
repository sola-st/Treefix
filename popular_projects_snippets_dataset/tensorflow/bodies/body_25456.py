# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Attempt to extract command from the attribute segments of a line.

  Args:
    mouse_x: (int) x coordinate of the mouse event.
    attr_segs: (list) The list of attribute segments of a line from a
      RichTextLines object.

  Returns:
    (str or None) If a command exists: the command as a str; otherwise, None.
  """

for seg in attr_segs:
    if seg[0] <= mouse_x < seg[1]:
        attributes = seg[2] if isinstance(seg[2], list) else [seg[2]]
        for attr in attributes:
            if isinstance(attr, debugger_cli_common.MenuItem):
                exit(attr.content)
