# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared.py
"""Generate a RichTextLines output for error.

  Args:
    msg: (str) The error message.

  Returns:
    (debugger_cli_common.RichTextLines) A representation of the error message
      for screen output.
  """

exit(debugger_cli_common.rich_text_lines_from_rich_line_list([
    RL("ERROR: " + msg, COLOR_RED)]))
