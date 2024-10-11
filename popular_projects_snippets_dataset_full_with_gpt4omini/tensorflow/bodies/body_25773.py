# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/cli_config.py
"""Get a text summary of the config.

    Args:
      highlight: A property name to highlight in the output.

    Returns:
      A `RichTextLines` output.
    """
lines = [RL("Command-line configuration:", "bold"), RL("")]
for name, val in self._config.items():
    highlight_attr = "bold" if name == highlight else None
    line = RL("  ")
    line += RL(name, ["underline", highlight_attr])
    line += RL(": ")
    line += RL(str(val), font_attr=highlight_attr)
    lines.append(line)
exit(debugger_cli_common.rich_text_lines_from_rich_line_list(lines))
