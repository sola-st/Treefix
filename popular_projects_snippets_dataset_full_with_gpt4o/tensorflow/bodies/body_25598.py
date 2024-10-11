# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
"""Print the content of a source file."""
del screen_info  # Unused.

parsed = self._arg_parsers["print_source"].parse_args(args)

source_annotation = source_utils.annotate_source(
    self._debug_dump,
    parsed.source_file_path,
    do_dumped_tensors=parsed.tensors)

source_lines, line_num_width = source_utils.load_source(
    parsed.source_file_path)

labeled_source_lines = []
actual_initial_scroll_target = 0
for i, line in enumerate(source_lines):
    annotated_line = RL("L%d" % (i + 1), cli_shared.COLOR_YELLOW)
    annotated_line += " " * (line_num_width - len(annotated_line))
    annotated_line += line
    labeled_source_lines.append(annotated_line)

    if i + 1 == parsed.line_begin:
        actual_initial_scroll_target = len(labeled_source_lines) - 1

    if i + 1 in source_annotation:
        sorted_elements = sorted(source_annotation[i + 1])
        for k, element in enumerate(sorted_elements):
            if k >= parsed.max_elements_per_line:
                omitted_info_line = RL("    (... Omitted %d of %d %s ...) " % (
                    len(sorted_elements) - parsed.max_elements_per_line,
                    len(sorted_elements),
                    "tensor(s)" if parsed.tensors else "op(s)"))
                omitted_info_line += RL(
                    "+5",
                    debugger_cli_common.MenuItem(
                        None,
                        self._reconstruct_print_source_command(
                            parsed, i + 1, max_elements_per_line_increase=5)))
                labeled_source_lines.append(omitted_info_line)
                break

            label = RL(" " * 4)
            if self._debug_dump.debug_watch_keys(
                debug_graphs.get_node_name(element)):
                attribute = debugger_cli_common.MenuItem("", "pt %s" % element)
            else:
                attribute = cli_shared.COLOR_BLUE

            label += RL(element, attribute)
            labeled_source_lines.append(label)

output = debugger_cli_common.rich_text_lines_from_rich_line_list(
    labeled_source_lines,
    annotations={debugger_cli_common.INIT_SCROLL_POS_KEY:
                 actual_initial_scroll_target})
_add_main_menu(output, node_name=None)
exit(output)
