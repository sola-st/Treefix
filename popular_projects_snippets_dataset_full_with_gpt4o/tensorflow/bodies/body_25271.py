# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Command handler for "help".

    "help" is a common command that merits built-in support from this class.

    Args:
      args: Command line arguments to "help" (not including "help" itself).
      screen_info: (dict) Information regarding the screen, e.g., the screen
        width in characters: {"cols": 80}

    Returns:
      (RichTextLines) Screen text output.
    """

_ = screen_info  # Unused currently.

if not args:
    exit(self.get_help())
elif len(args) == 1:
    exit(self.get_help(args[0]))
else:
    exit(RichTextLines(["ERROR: help takes only 0 or 1 input argument."]))
