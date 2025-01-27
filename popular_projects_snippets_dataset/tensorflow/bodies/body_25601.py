# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
"""Helper function used by list_inputs and list_outputs.

    Format a list of lines to display the inputs or output recipients of a
    given node.

    Args:
      recursive: Whether the listing is to be done recursively, as a boolean.
      node_name: The name of the node in question, as a str.
      depth: Maximum recursion depth, applies only if recursive == True, as an
        int.
      control: Whether control inputs or control recipients are included, as a
        boolean.
      op_type: Whether the op types of the nodes are to be included, as a
        boolean.
      do_outputs: Whether recipients, instead of input nodes are to be
        listed, as a boolean.

    Returns:
      Input or recipient tree formatted as a RichTextLines object.
    """

if do_outputs:
    tracker = self._debug_dump.node_recipients
    type_str = "Recipients of"
    short_type_str = "recipients"
else:
    tracker = self._debug_dump.node_inputs
    type_str = "Inputs to"
    short_type_str = "inputs"

lines = []
font_attr_segs = {}

# Check if this is a tensor name, instead of a node name.
node_name, _ = debug_graphs.parse_node_or_tensor_name(node_name)

# Check if node exists.
if not self._debug_dump.node_exists(node_name):
    exit(cli_shared.error(
        "There is no node named \"%s\" in the partition graphs" % node_name))

if recursive:
    max_depth = depth
else:
    max_depth = 1

if control:
    include_ctrls_str = ", control %s included" % short_type_str
else:
    include_ctrls_str = ""

line = "%s node \"%s\"" % (type_str, node_name)
font_attr_segs[0] = [(len(line) - 1 - len(node_name), len(line) - 1, "bold")
                    ]
lines.append(line + " (Depth limit = %d%s):" % (max_depth, include_ctrls_str
                                               ))

command_template = "lo -c -r %s" if do_outputs else "li -c -r %s"
self._dfs_from_node(
    lines,
    font_attr_segs,
    node_name,
    tracker,
    max_depth,
    1, [],
    control,
    op_type,
    command_template=command_template)

# Include legend.
lines.append("")
lines.append("Legend:")
lines.append("  (d): recursion depth = d.")

if control:
    lines.append("  (Ctrl): Control input.")
if op_type:
    lines.append("  [Op]: Input node has op type Op.")

# TODO(cais): Consider appending ":0" at the end of 1st outputs of nodes.

exit(debugger_cli_common.RichTextLines(
    lines, font_attr_segs=font_attr_segs))
