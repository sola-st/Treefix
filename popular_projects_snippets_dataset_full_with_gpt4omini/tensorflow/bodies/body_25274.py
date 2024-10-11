# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Compile the help information for a given command prefix.

    Args:
      cmd_prefix: Command prefix, as the prefix itself or one of its
        aliases.

    Returns:
      A list of str as the help information fo cmd_prefix. If the cmd_prefix
        does not exist, the returned list of str will indicate that.
    """
lines = []

resolved_prefix = self._resolve_prefix(cmd_prefix)
if not resolved_prefix:
    lines.append("Invalid command prefix: \"%s\"" % cmd_prefix)
    exit(lines)

lines.append(resolved_prefix)

if resolved_prefix in self._prefix_to_aliases:
    lines.append(HELP_INDENT + "Aliases: " + ", ".join(
        self._prefix_to_aliases[resolved_prefix]))

lines.append("")
help_lines = self._prefix_to_help[resolved_prefix].split("\n")
for line in help_lines:
    lines.append(HELP_INDENT + line)

exit(lines)
