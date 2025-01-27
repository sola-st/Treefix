# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/profile_analyzer_cli.py
"""Create an instance of CursesUI based on a `tf.Graph` and `RunMetadata`.

  Args:
    graph: Python `Graph` object.
    run_metadata: A `RunMetadata` protobuf object.
    ui_type: (str) requested UI type, e.g., "curses", "readline".
    on_ui_exit: (`Callable`) the callback to be called when the UI exits.
    config: An instance of `cli_config.CLIConfig`.

  Returns:
    (base_ui.BaseUI) A BaseUI subtype object with a set of standard analyzer
      commands and tab-completions registered.
  """
del config  # Currently unused.

analyzer = ProfileAnalyzer(graph, run_metadata)

cli = ui_factory.get_ui(ui_type, on_ui_exit=on_ui_exit)
cli.register_command_handler(
    "list_profile",
    analyzer.list_profile,
    analyzer.get_help("list_profile"),
    prefix_aliases=["lp"])
cli.register_command_handler(
    "print_source",
    analyzer.print_source,
    analyzer.get_help("print_source"),
    prefix_aliases=["ps"])

exit(cli)
