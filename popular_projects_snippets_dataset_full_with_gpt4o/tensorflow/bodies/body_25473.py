# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Create command textbox on screen.

    Args:
      existing_command: (str) A command string to put in the textbox right
        after its creation.
    """

# Display the tfdbg prompt.
self._addstr(self._max_y - self._command_textbox_height, 0,
             self.CLI_PROMPT, curses.A_BOLD)
self._stdscr.refresh()

self._command_window.clear()

# Command text box.
self._command_textbox = textpad.Textbox(
    self._command_window, insert_mode=True)

# Enter existing command.
self._auto_key_in(existing_command)
