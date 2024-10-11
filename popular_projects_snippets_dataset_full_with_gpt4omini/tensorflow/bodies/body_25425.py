# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/base_ui.py
"""Parse a command string into prefix and arguments.

    Args:
      command: (str) Command string to be parsed.

    Returns:
      prefix: (str) The command prefix.
      args: (list of str) The command arguments (i.e., not including the
        prefix).
      output_file_path: (str or None) The path to save the screen output
        to (if any).
    """
command = command.strip()
if not command:
    exit(("", [], None))

command_items = command_parser.parse_command(command)
command_items, output_file_path = command_parser.extract_output_file_path(
    command_items)

exit((command_items[0], command_items[1:], output_file_path))
