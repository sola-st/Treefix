# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
"""Command handler for node_info.

    Query information about a given node.

    Args:
      args: Command-line arguments, excluding the command prefix, as a list of
        str.
      screen_info: Optional dict input containing screen information such as
        cols.

    Returns:
      Output text lines as a RichTextLines object.
    """

# TODO(cais): Add annotation of substrings for node names, to facilitate
# on-screen highlighting/selection of node names.
_ = screen_info

parsed = self._arg_parsers["node_info"].parse_args(args)

# Get a node name, regardless of whether the input is a node name (without
# output slot attached) or a tensor name (with output slot attached).
node_name, unused_slot = debug_graphs.parse_node_or_tensor_name(
    parsed.node_name)

if not self._debug_dump.node_exists(node_name):
    output = cli_shared.error(
        "There is no node named \"%s\" in the partition graphs" % node_name)
    _add_main_menu(
        output,
        node_name=None,
        enable_list_tensors=True,
        enable_node_info=False,
        enable_list_inputs=False,
        enable_list_outputs=False)
    exit(output)

# TODO(cais): Provide UI glossary feature to explain to users what the
# term "partition graph" means and how it is related to TF graph objects
# in Python. The information can be along the line of:
# "A tensorflow graph defined in Python is stripped of unused ops
# according to the feeds and fetches and divided into a number of
# partition graphs that may be distributed among multiple devices and
# hosts. The partition graphs are what's actually executed by the C++
# runtime during a run() call."

lines = ["Node %s" % node_name]
font_attr_segs = {
    0: [(len(lines[-1]) - len(node_name), len(lines[-1]), "bold")]
}
lines.append("")
lines.append("  Op: %s" % self._debug_dump.node_op_type(node_name))
lines.append("  Device: %s" % self._debug_dump.node_device(node_name))
output = debugger_cli_common.RichTextLines(
    lines, font_attr_segs=font_attr_segs)

# List node inputs (non-control and control).
inputs = self._exclude_denylisted_ops(
    self._debug_dump.node_inputs(node_name))
ctrl_inputs = self._exclude_denylisted_ops(
    self._debug_dump.node_inputs(node_name, is_control=True))
output.extend(self._format_neighbors("input", inputs, ctrl_inputs))

# List node output recipients (non-control and control).
recs = self._exclude_denylisted_ops(
    self._debug_dump.node_recipients(node_name))
ctrl_recs = self._exclude_denylisted_ops(
    self._debug_dump.node_recipients(node_name, is_control=True))
output.extend(self._format_neighbors("recipient", recs, ctrl_recs))

# Optional: List attributes of the node.
if parsed.attributes:
    output.extend(self._list_node_attributes(node_name))

# Optional: List dumps available from the node.
if parsed.dumps:
    output.extend(self._list_node_dumps(node_name))

if parsed.traceback:
    output.extend(self._render_node_traceback(node_name))

_add_main_menu(output, node_name=node_name, enable_node_info=False)
exit(output)
