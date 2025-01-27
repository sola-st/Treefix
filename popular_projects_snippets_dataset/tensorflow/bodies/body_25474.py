# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Command-line UI loop.

    Returns:
      An exit token of arbitrary type. The token can be None.
    """

while True:
    # Enter history command if pointer is in history (> 0):
    if self._command_pointer > 0:
        existing_command = self._active_command_history[-self._command_pointer]
    else:
        existing_command = self._pending_command
    self._screen_create_command_textbox(existing_command)

    try:
        command, terminator, pending_command_changed = self._get_user_command()
    except debugger_cli_common.CommandLineExit as e:
        exit(e.exit_token)

    if not command and terminator != self.CLI_TAB_KEY:
        continue

    if terminator in self.CLI_CR_KEYS or terminator == curses.KEY_MOUSE:
        exit_token = self._dispatch_command(command)
        if exit_token is not None:
            exit(exit_token)
    elif terminator == self.CLI_TAB_KEY:
        tab_completed = self._tab_complete(command)
        self._pending_command = tab_completed
        self._cmd_ptr = 0
    elif pending_command_changed:
        self._pending_command = command

exit()
