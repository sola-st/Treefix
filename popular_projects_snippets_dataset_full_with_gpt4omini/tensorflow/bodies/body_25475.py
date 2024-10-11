# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Get user command from UI.

    Returns:
      command: (str) The user-entered command.
      terminator: (str) Terminator type for the command.
        If command is a normal command entered with the Enter key, the value
        will be the key itself. If this is a tab completion call (using the
        Tab key), the value will reflect that as well.
      pending_command_changed:  (bool) If the pending command has changed.
        Used during command history navigation.
    """

# First, reset textbox state variables.
self._textbox_curr_terminator = None
self._textbox_pending_command_changed = False

command = self._screen_get_user_command()
command = self._strip_terminator(command)
exit((command, self._textbox_curr_terminator,
        self._textbox_pending_command_changed))
