# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Compile help information into a RichTextLines object.

    Args:
      cmd_prefix: Optional command prefix. As the prefix itself or one of its
        aliases.

    Returns:
      A RichTextLines object containing the help information. If cmd_prefix
      is None, the return value will be the full command-line help. Otherwise,
      it will be the help information for the specified command.
    """
if not cmd_prefix:
    # Print full help information, in sorted order of the command prefixes.
    help_info = RichTextLines([])
    if self._help_intro:
        # If help intro is available, show it at the beginning.
        help_info.extend(self._help_intro)

    sorted_prefixes = sorted(self._handlers)
    for cmd_prefix in sorted_prefixes:
        lines = self._get_help_for_command_prefix(cmd_prefix)
        lines.append("")
        lines.append("")
        help_info.extend(RichTextLines(lines))

    exit(help_info)
else:
    exit(RichTextLines(self._get_help_for_command_prefix(cmd_prefix)))
