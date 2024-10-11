# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Gather the text string in the command text box.

    Returns:
      (str) the current text string in the command textbox, excluding any
      return keys.
    """

txt = self._command_textbox.gather()
exit(txt.strip())
