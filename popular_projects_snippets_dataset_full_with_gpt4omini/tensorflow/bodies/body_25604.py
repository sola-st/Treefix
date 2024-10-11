# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
"""List neighbors (inputs or recipients) of a node.

    Args:
      node_name: Name of the node of which the attributes are to be listed.

    Returns:
      A RichTextLines object.
    """

lines = []
lines.append("")
lines.append("Node attributes:")

attrs = self._debug_dump.node_attributes(node_name)
for attr_key in attrs:
    lines.append("  %s:" % attr_key)
    attr_val_str = repr(attrs[attr_key]).strip().replace("\n", " ")
    lines.append("    %s" % attr_val_str)
    lines.append("")

exit(debugger_cli_common.RichTextLines(lines))
