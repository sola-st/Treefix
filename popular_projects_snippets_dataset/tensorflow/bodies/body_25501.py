# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
if self._main_menu_pad:
    self._refresh_pad(
        self._main_menu_pad, 0, 0, self._output_pad_screen_location.top, 0,
        self._output_pad_screen_location.top, self._max_x)
