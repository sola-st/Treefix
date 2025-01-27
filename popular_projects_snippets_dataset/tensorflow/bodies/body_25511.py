# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
del signal_num  # Unused.
del frame  # Unused.

if self._on_ui_exit:
    self._on_ui_exit()

self._screen_terminate()
print("\ntfdbg: caught SIGINT; calling sys.exit(1).", file=sys.stderr)
sys.exit(1)
