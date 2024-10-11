# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli_test.py
"""Create an analyzer CLI.

  Args:
    dump: A `DebugDumpDir` object to base the analyzer CLI on.

  Returns:
    1) A `DebugAnalyzer` object created based on `dump`.
    2) A `CommandHandlerRegistry` that is based on the `DebugAnalyzer` object
       and has the common tfdbg commands, e.g., lt, ni, li, lo, registered.
  """
# Construct the analyzer.
analyzer = analyzer_cli.DebugAnalyzer(dump, _cli_config_from_temp_file())

# Construct the handler registry.
registry = debugger_cli_common.CommandHandlerRegistry()

# Register command handlers.
registry.register_command_handler(
    "list_tensors",
    analyzer.list_tensors,
    analyzer.get_help("list_tensors"),
    prefix_aliases=["lt"])
registry.register_command_handler(
    "node_info",
    analyzer.node_info,
    analyzer.get_help("node_info"),
    prefix_aliases=["ni"])
registry.register_command_handler(
    "list_inputs",
    analyzer.list_inputs,
    analyzer.get_help("list_inputs"),
    prefix_aliases=["li"])
registry.register_command_handler(
    "list_outputs",
    analyzer.list_outputs,
    analyzer.get_help("list_outputs"),
    prefix_aliases=["lo"])
registry.register_command_handler(
    "print_tensor",
    analyzer.print_tensor,
    analyzer.get_help("print_tensor"),
    prefix_aliases=["pt"])
registry.register_command_handler(
    "print_source",
    analyzer.print_source,
    analyzer.get_help("print_source"),
    prefix_aliases=["ps"])
registry.register_command_handler(
    "list_source",
    analyzer.list_source,
    analyzer.get_help("list_source"),
    prefix_aliases=["ls"])
registry.register_command_handler(
    "eval",
    analyzer.evaluate_expression,
    analyzer.get_help("eval"),
    prefix_aliases=["ev"])

exit((analyzer, registry))
