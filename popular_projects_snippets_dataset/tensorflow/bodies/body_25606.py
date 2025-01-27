# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
"""Create an instance of CursesUI based on a DebugDumpDir object.

  Args:
    debug_dump: (debug_data.DebugDumpDir) The debug dump to use.
    tensor_filters: (dict) A dict mapping tensor filter name (str) to tensor
      filter (Callable).
    ui_type: (str) requested UI type, e.g., "curses", "readline".
    on_ui_exit: (`Callable`) the callback to be called when the UI exits.
    config: A `cli_config.CLIConfig` object.

  Returns:
    (base_ui.BaseUI) A BaseUI subtype object with a set of standard analyzer
      commands and tab-completions registered.
  """
if config is None:
    config = cli_config.CLIConfig()

analyzer = DebugAnalyzer(debug_dump, config=config)
if tensor_filters:
    for tensor_filter_name in tensor_filters:
        analyzer.add_tensor_filter(
            tensor_filter_name, tensor_filters[tensor_filter_name])

cli = ui_factory.get_ui(ui_type, on_ui_exit=on_ui_exit, config=config)
cli.register_command_handler(
    "list_tensors",
    analyzer.list_tensors,
    analyzer.get_help("list_tensors"),
    prefix_aliases=["lt"])
cli.register_command_handler(
    "node_info",
    analyzer.node_info,
    analyzer.get_help("node_info"),
    prefix_aliases=["ni"])
cli.register_command_handler(
    "list_inputs",
    analyzer.list_inputs,
    analyzer.get_help("list_inputs"),
    prefix_aliases=["li"])
cli.register_command_handler(
    "list_outputs",
    analyzer.list_outputs,
    analyzer.get_help("list_outputs"),
    prefix_aliases=["lo"])
cli.register_command_handler(
    "print_tensor",
    analyzer.print_tensor,
    analyzer.get_help("print_tensor"),
    prefix_aliases=["pt"])
cli.register_command_handler(
    "print_source",
    analyzer.print_source,
    analyzer.get_help("print_source"),
    prefix_aliases=["ps"])
cli.register_command_handler(
    "list_source",
    analyzer.list_source,
    analyzer.get_help("list_source"),
    prefix_aliases=["ls"])
cli.register_command_handler(
    "eval",
    analyzer.evaluate_expression,
    analyzer.get_help("eval"),
    prefix_aliases=["ev"])

dumped_tensor_names = []
for datum in debug_dump.dumped_tensor_data:
    dumped_tensor_names.append("%s:%d" % (datum.node_name, datum.output_slot))

# Tab completions for command "print_tensors".
cli.register_tab_comp_context(["print_tensor", "pt"], dumped_tensor_names)

exit(cli)
