# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
try:
    pad.refresh(*args)
except curses.error:
    pass
