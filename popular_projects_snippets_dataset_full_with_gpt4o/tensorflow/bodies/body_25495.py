# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Display main menu associated with screen output, if the menu exists.

    Args:
      output: (debugger_cli_common.RichTextLines) The RichTextLines output from
        the annotations field of which the menu will be extracted and used (if
        the menu exists).
    """

if debugger_cli_common.MAIN_MENU_KEY in output.annotations:
    self._main_menu = output.annotations[
        debugger_cli_common.MAIN_MENU_KEY].format_as_single_line(
            prefix="| ", divider=" | ", enabled_item_attrs=["underline"])

    self._main_menu_pad = self._screen_new_output_pad(1, self._max_x - 2)

    # The unwrapped menu line may exceed screen width, in which case it needs
    # to be cut off.
    wrapped_menu, _ = debugger_cli_common.wrap_rich_text_lines(
        self._main_menu, self._max_x - 3)
    self._screen_add_line_to_output_pad(
        self._main_menu_pad,
        0,
        wrapped_menu.lines[0],
        color_segments=(wrapped_menu.font_attr_segs[0]
                        if 0 in wrapped_menu.font_attr_segs else None))
else:
    self._main_menu = None
    self._main_menu_pad = None
