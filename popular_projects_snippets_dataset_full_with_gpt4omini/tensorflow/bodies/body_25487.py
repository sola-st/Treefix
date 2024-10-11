# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Automatically key in a command to the command Textbox.

    Args:
      command: The command, as a string or None.
      erase_existing: (bool) whether existing text (if any) is to be erased
          first.
    """
if erase_existing:
    self._erase_existing_command()

command = command or ""
for c in command:
    self._command_textbox.do_command(ord(c))
