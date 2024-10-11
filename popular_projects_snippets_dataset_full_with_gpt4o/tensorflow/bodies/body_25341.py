# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
"""Override to insert observer of existing commands.

    Used in testing of history navigation and tab completion.

    Args:
      existing_command: Command string entered to the textbox at textbox
        creation time. Note that the textbox does not actually exist in this
        mock subclass. This method only keeps track of and records the state.
    """

self.existing_commands.append(existing_command)
self._curr_existing_command = existing_command
