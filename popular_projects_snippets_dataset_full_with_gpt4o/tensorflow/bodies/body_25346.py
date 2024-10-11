# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
command = self._command_sequence[self._command_counter]

self._command_key_counter = 0
for c in command:
    if c == curses.KEY_RESIZE:
        # Special case for simulating a terminal resize event in curses.
        self._height = command[1]
        self._width = command[2]
        self._on_textbox_keypress(c)
        self._command_counter += 1
        exit("")
    elif c == curses.KEY_MOUSE:
        mouse_x = command[1]
        mouse_y = command[2]
        self._command_counter += 1
        self._textbox_curr_terminator = c
        exit(self._fetch_hyperlink_command(mouse_x, mouse_y))
    else:
        y = self._on_textbox_keypress(c)

        self._command_key_counter += 1
        if y == curses_ui.CursesUI.CLI_TERMINATOR_KEY:
            break

self._command_counter += 1

# Take into account pre-existing string automatically entered on textbox
# creation.
exit(self._curr_existing_command + codes_to_string(command))
