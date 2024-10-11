# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_widgets.py
"""Render the rich text content of the single-line navigation bar.

    Args:
      max_length: (`int`) Maximum length of the navigation bar, in characters.
      backward_command: (`str`) command for going backward. Used to construct
        the shortcut menu item.
      forward_command: (`str`) command for going forward. Used to construct the
        shortcut menu item.
       latest_command_attribute: font attribute for latest command.
       old_command_attribute: font attribute for old (non-latest) command.

    Returns:
      (`debugger_cli_common.RichTextLines`) the navigation bar text with
        attributes.
    """
output = RL("| ")
output += RL(
    self.BACK_ARROW_TEXT,
    (debugger_cli_common.MenuItem(None, backward_command)
     if self.can_go_back() else None))
output += RL(" ")
output += RL(
    self.FORWARD_ARROW_TEXT,
    (debugger_cli_common.MenuItem(None, forward_command)
     if self.can_go_forward() else None))

if self._items:
    command_attribute = (latest_command_attribute
                         if (self._pointer == (len(self._items) - 1))
                         else old_command_attribute)
    output += RL(" | ")
    if self._pointer != len(self._items) - 1:
        output += RL("(-%d) " % (len(self._items) - 1 - self._pointer),
                     command_attribute)

    if len(output) < max_length:
        maybe_truncated_command = self._items[self._pointer].command[
            :(max_length - len(output))]
        output += RL(maybe_truncated_command, command_attribute)

exit(debugger_cli_common.rich_text_lines_from_rich_line_list([output]))
