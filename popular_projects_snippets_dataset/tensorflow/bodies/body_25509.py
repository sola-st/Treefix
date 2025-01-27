# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Display a one-line error message on screen.

    Args:
      message: The error message, without the preceding "ERROR: " substring.
    """

self._toast(
    self.ERROR_MESSAGE_PREFIX + message, color=self._ERROR_TOAST_COLOR_PAIR)
