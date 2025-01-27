# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Dispatch user command.

    Args:
      command: (str) Command to dispatch.

    Returns:
      An exit token object. None value means that the UI loop should not exit.
      A non-None value means the UI loop should exit.
    """

if self._output_pad:
    self._toast(self._UI_WAIT_MESSAGE, color=self._UI_WAIT_COLOR_PAIR)

if command in self.CLI_EXIT_COMMANDS:
    # Explicit user command-triggered exit: EXPLICIT_USER_EXIT as the exit
    # token.
    exit(debugger_cli_common.EXPLICIT_USER_EXIT)
elif (command == self._NAVIGATION_FORWARD_COMMAND or
      command == self._NAVIGATION_BACK_COMMAND):
    self._navigate_screen_output(command)
    exit()

if command:
    self._command_history_store.add_command(command)

if (command.startswith(self.REGEX_SEARCH_PREFIX) and
    self._curr_unwrapped_output):
    if len(command) > len(self.REGEX_SEARCH_PREFIX):
        # Command is like "/regex". Perform regex search.
        regex = command[len(self.REGEX_SEARCH_PREFIX):]

        self._curr_search_regex = regex
        self._display_output(self._curr_unwrapped_output, highlight_regex=regex)
    elif self._unwrapped_regex_match_lines:
        # Command is "/". Continue scrolling down matching lines.
        self._display_output(
            self._curr_unwrapped_output,
            is_refresh=True,
            highlight_regex=self._curr_search_regex)

    self._command_pointer = 0
    self._pending_command = ""
    exit()
elif command.startswith(self.TENSOR_INDICES_NAVIGATION_PREFIX):
    indices_str = command[1:].strip()
    if indices_str:
        try:
            indices = command_parser.parse_indices(indices_str)
            omitted, line_index, _, _ = tensor_format.locate_tensor_element(
                self._curr_wrapped_output, indices)
            if not omitted:
                self._scroll_output(
                    _SCROLL_TO_LINE_INDEX, line_index=line_index)
        except Exception as e:  # pylint: disable=broad-except
            self._error_toast(str(e))
    else:
        self._error_toast("Empty indices.")

    exit()

try:
    prefix, args, output_file_path = self._parse_command(command)
except SyntaxError as e:
    self._error_toast(str(e))
    exit()

if not prefix:
    # Empty command: take no action. Should not exit.
    exit()

# Take into account scroll bar width.
screen_info = {"cols": self._max_x - 2}
exit_token = None
if self._command_handler_registry.is_registered(prefix):
    try:
        screen_output = self._command_handler_registry.dispatch_command(
            prefix, args, screen_info=screen_info)
    except debugger_cli_common.CommandLineExit as e:
        exit_token = e.exit_token
else:
    screen_output = debugger_cli_common.RichTextLines([
        self.ERROR_MESSAGE_PREFIX + "Invalid command prefix \"%s\"" % prefix
    ])

# Clear active command history. Until next up/down history navigation
# occurs, it will stay empty.
self._active_command_history = []

if exit_token is not None:
    exit(exit_token)

self._nav_history.add_item(command, screen_output, 0)

self._display_output(screen_output)
if output_file_path:
    try:
        screen_output.write_to_file(output_file_path)
        self._info_toast("Wrote output to %s" % output_file_path)
    except Exception:  # pylint: disable=broad-except
        self._error_toast("Failed to write output to %s" % output_file_path)

self._command_pointer = 0
self._pending_command = ""
