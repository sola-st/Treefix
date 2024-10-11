# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
"""List neighbors (inputs or recipients) of a node.

    Args:
      neighbor_type: ("input" | "recipient")
      non_ctrls: Non-control neighbor node names, as a list of str.
      ctrls: Control neighbor node names, as a list of str.

    Returns:
      A RichTextLines object.
    """

# TODO(cais): Return RichTextLines instead, to allow annotation of node
# names.
lines = []
font_attr_segs = {}

lines.append("")
lines.append("  %d %s(s) + %d control %s(s):" %
             (len(non_ctrls), neighbor_type, len(ctrls), neighbor_type))
lines.append("    %d %s(s):" % (len(non_ctrls), neighbor_type))
for non_ctrl in non_ctrls:
    line = "      [%s] %s" % (self._debug_dump.node_op_type(non_ctrl),
                              non_ctrl)
    lines.append(line)
    font_attr_segs[len(lines) - 1] = [(
        len(line) - len(non_ctrl), len(line),
        debugger_cli_common.MenuItem(None, "ni -a -d -t %s" % non_ctrl))]

if ctrls:
    lines.append("")
    lines.append("    %d control %s(s):" % (len(ctrls), neighbor_type))
    for ctrl in ctrls:
        line = "      [%s] %s" % (self._debug_dump.node_op_type(ctrl), ctrl)
        lines.append(line)
        font_attr_segs[len(lines) - 1] = [(
            len(line) - len(ctrl), len(line),
            debugger_cli_common.MenuItem(None, "ni -a -d -t %s" % ctrl))]

exit(debugger_cli_common.RichTextLines(
    lines, font_attr_segs=font_attr_segs))
