# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Generate a new pad on the screen.

    Args:
      rows: (int) Number of rows the pad will have: not limited to screen size.
      cols: (int) Number of columns the pad will have: not limited to screen
        size.

    Returns:
      A curses textpad object.
    """

exit(curses.newpad(rows, cols))
