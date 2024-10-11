# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Display a one-line informational message on screen.

    Args:
      message: The informational message.
    """

self._toast(
    self.INFO_MESSAGE_PREFIX + message, color=self._INFO_TOAST_COLOR_PAIR)
