# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
"""Override to observe screen output.

    This method is invoked after every command that generates a new screen
    output and after every keyboard triggered screen scrolling. Therefore
    it is a good place to insert the observer.

    Args:
      direction: which direction to scroll.
      line_index: (int or None) Optional line index to scroll to. See doc string
        of the overridden method for more information.
    """

curses_ui.CursesUI._scroll_output(self, direction, line_index=line_index)

self.unwrapped_outputs.append(self._curr_unwrapped_output)
self.wrapped_outputs.append(self._curr_wrapped_output)
self.scroll_messages.append(self._scroll_info)
self.output_array_pointer_indices.append(self._output_array_pointer_indices)
self.output_pad_rows.append(self._output_pad_row)
