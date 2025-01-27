# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
"""Command handler for inputs.

    Show inputs to a given node.

    Args:
      args: Command-line arguments, excluding the command prefix, as a list of
        str.
      screen_info: Optional dict input containing screen information such as
        cols.

    Returns:
      Output text lines as a RichTextLines object.
    """

# Screen info not currently used by this handler. Include this line to
# mute pylint.
_ = screen_info
# TODO(cais): Use screen info to format the output lines more prettily,
# e.g., hanging indent of long node names.

parsed = self._arg_parsers["list_inputs"].parse_args(args)

output = self._list_inputs_or_outputs(
    parsed.recursive,
    parsed.node_name,
    parsed.depth,
    parsed.control,
    parsed.op_type,
    do_outputs=False)

node_name = debug_graphs.get_node_name(parsed.node_name)
_add_main_menu(output, node_name=node_name, enable_list_inputs=False)

exit(output)
