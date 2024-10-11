# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Terminate the curses screen."""

self._stdscr.keypad(0)
curses.nocbreak()
curses.echo()
curses.endwin()

try:
    # Remove SIGINT handler.
    signal.signal(signal.SIGINT, signal.SIG_DFL)
except ValueError:
    # Can't catch signals unless you're the main thread.
    pass
