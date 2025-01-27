# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
"""Render traceback of a node's creation in Python, if available.

    Args:
      node_name: (str) name of the node.

    Returns:
      A RichTextLines object containing the stack trace of the node's
      construction.
    """

lines = [RL(""), RL(""), RL("Traceback of node construction:", "bold")]

try:
    node_stack = self._debug_dump.node_traceback(node_name)
    for depth, (file_path, line, function_name, text) in enumerate(
        node_stack):
        lines.append("%d: %s" % (depth, file_path))

        attribute = debugger_cli_common.MenuItem(
            "", "ps %s -b %d" % (file_path, line)) if text else None
        line_number_line = RL("  ")
        line_number_line += RL("Line:     %d" % line, attribute)
        lines.append(line_number_line)

        lines.append("  Function: %s" % function_name)
        lines.append("  Text:     " + (("\"%s\"" % text) if text else "None"))
        lines.append("")
except KeyError:
    lines.append("(Node unavailable in the loaded Python graph)")
except LookupError:
    lines.append("(Unavailable because no Python graph has been loaded)")

exit(debugger_cli_common.rich_text_lines_from_rich_line_list(lines))
