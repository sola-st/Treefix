# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
if self._curr_unwrapped_output is not None:
    self._display_nav_bar()
    self._display_main_menu(self._curr_unwrapped_output)
    self._display_output(self._curr_unwrapped_output, is_refresh=True)
