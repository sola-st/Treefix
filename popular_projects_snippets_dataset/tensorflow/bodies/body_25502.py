# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Compile status summary about this Curses UI instance.

    The information includes: scroll status and mouse ON/OFF status.

    Returns:
      (str) A single text line summarizing the UI status, adapted to the
        current screen width.
    """

info = ""
if self._output_pad_height > self._output_pad_screen_height + 1:
    # Display information about the scrolling of tall screen output.
    scroll_percentage = 100.0 * (min(
        1.0,
        float(self._output_pad_row) /
        (self._output_pad_height - self._output_pad_screen_height - 1)))
    if self._output_pad_row == 0:
        scroll_directions = " (PgDn)"
    elif self._output_pad_row >= (
        self._output_pad_height - self._output_pad_screen_height - 1):
        scroll_directions = " (PgUp)"
    else:
        scroll_directions = " (PgDn/PgUp)"

    info += "--- Scroll%s: %.2f%% " % (scroll_directions, scroll_percentage)

self._output_array_pointer_indices = self._show_array_indices()

# Add array indices information to scroll message.
if self._output_array_pointer_indices:
    if self._output_array_pointer_indices[0]:
        info += self._format_indices(self._output_array_pointer_indices[0])
    info += "-"
    if self._output_array_pointer_indices[-1]:
        info += self._format_indices(self._output_array_pointer_indices[-1])
    info += " "

# Add mouse mode information.
mouse_mode_str = "Mouse: "
mouse_mode_str += "ON" if self._mouse_enabled else "OFF"

if len(info) + len(mouse_mode_str) + 5 < self._max_x:
    info += "-" * (self._max_x - len(info) - len(mouse_mode_str) - 4)
    info += " "
    info += mouse_mode_str
    info += " ---"
else:
    info += "-" * (self._max_x - len(info))

exit(info)
