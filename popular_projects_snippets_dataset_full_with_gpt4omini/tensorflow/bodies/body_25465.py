# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Launch the curses screen."""

curses.noecho()
curses.cbreak()
self._stdscr.keypad(1)

self._mouse_enabled = self.config.get("mouse_mode")
self._screen_set_mousemask()
self.config.set_callback(
    "mouse_mode",
    lambda cfg: self._set_mouse_enabled(cfg.get("mouse_mode")))

self._screen_create_command_window()
