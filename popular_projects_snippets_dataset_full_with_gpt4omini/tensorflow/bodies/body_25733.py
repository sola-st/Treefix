# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_shared.py
"""Generate a RichTextLines object that describes a recommended command.

  Args:
    command: (str) The command to recommend.
    description: (str) A description of what the command does.
    indent: (int) How many spaces to indent in the beginning.
    create_link: (bool) Whether a command link is to be applied to the command
      string.

  Returns:
    (RichTextLines) Formatted text (with font attributes) for recommending the
      command.
  """

indent_str = " " * indent

if create_link:
    font_attr = [debugger_cli_common.MenuItem("", command), "bold"]
else:
    font_attr = "bold"

lines = [RL(indent_str) + RL(command, font_attr) + ":",
         indent_str + "  " + description]

exit(debugger_cli_common.rich_text_lines_from_rich_line_list(lines))
