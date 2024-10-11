# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
"""List dumped tensor data from a node.

    Args:
      node_name: Name of the node of which the attributes are to be listed.

    Returns:
      A RichTextLines object.
    """

lines = []
font_attr_segs = {}

watch_keys = self._debug_dump.debug_watch_keys(node_name)

dump_count = 0
for watch_key in watch_keys:
    debug_tensor_data = self._debug_dump.watch_key_to_data(watch_key)
    for datum in debug_tensor_data:
        line = "  Slot %d @ %s @ %.3f ms" % (
            datum.output_slot, datum.debug_op,
            (datum.timestamp - self._debug_dump.t0) / 1000.0)
        lines.append(line)
        command = "pt %s:%d -n %d" % (node_name, datum.output_slot, dump_count)
        font_attr_segs[len(lines) - 1] = [(
            2, len(line), debugger_cli_common.MenuItem(None, command))]
        dump_count += 1

output = debugger_cli_common.RichTextLines(
    lines, font_attr_segs=font_attr_segs)
output_with_header = debugger_cli_common.RichTextLines(
    ["%d dumped tensor(s):" % dump_count, ""])
output_with_header.extend(output)
exit(output_with_header)
