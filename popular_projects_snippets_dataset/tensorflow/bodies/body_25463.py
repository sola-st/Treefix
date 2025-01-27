# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Screen initialization.

    Creates curses stdscr and initialize the color pairs for display.
    """
# If the terminal type is color-ready, enable it.
if os.getenv("COLORTERM") in _COLOR_READY_COLORTERMS:
    os.environ["TERM"] = _COLOR_ENABLED_TERM
self._stdscr = curses.initscr()
self._command_window = None
self._screen_color_init()
