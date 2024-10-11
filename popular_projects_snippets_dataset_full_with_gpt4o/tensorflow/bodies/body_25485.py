# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
output_top = self._output_top_row
if self._main_menu_pad:
    output_top += 1

if mouse_y == self._nav_bar_row and self._nav_bar:
    # Click was in the nav bar.
    exit(_get_command_from_line_attr_segs(mouse_x,
                                            self._nav_bar.font_attr_segs[0]))
elif mouse_y == self._output_top_row and self._main_menu_pad:
    # Click was in the menu bar.
    exit(_get_command_from_line_attr_segs(mouse_x,
                                            self._main_menu.font_attr_segs[0]))
else:
    absolute_mouse_y = mouse_y + self._output_pad_row - output_top
    if absolute_mouse_y in self._curr_wrapped_output.font_attr_segs:
        exit(_get_command_from_line_attr_segs(
            mouse_x, self._curr_wrapped_output.font_attr_segs[absolute_mouse_y]))
