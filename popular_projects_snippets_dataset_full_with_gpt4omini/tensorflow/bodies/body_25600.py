# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
"""List Python source files that constructed nodes and tensors."""
del screen_info  # Unused.

parsed = self._arg_parsers["list_source"].parse_args(args)
source_list = source_utils.list_source_files_against_dump(
    self._debug_dump,
    path_regex_allowlist=parsed.path_filter,
    node_name_regex_allowlist=parsed.node_name_filter)

top_lines = [
    RL("List of source files that created nodes in this run", "bold")]
if parsed.path_filter:
    top_lines.append(
        RL("File path regex filter: \"%s\"" % parsed.path_filter))
if parsed.node_name_filter:
    top_lines.append(
        RL("Node name regex filter: \"%s\"" % parsed.node_name_filter))
top_lines.append(RL())
output = debugger_cli_common.rich_text_lines_from_rich_line_list(top_lines)
if not source_list:
    output.append("[No source file information.]")
    exit(output)

output.extend(self._make_source_table(
    [item for item in source_list if not item[1]], False))
output.extend(self._make_source_table(
    [item for item in source_list if item[1]], True))
_add_main_menu(output, node_name=None)
exit(output)
