# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/base_ui.py
"""Constructor of the base class.

    Args:
      on_ui_exit: (`Callable`) the callback to be called when the UI exits.
      config: An instance of `cli_config.CLIConfig()` carrying user-facing
        configurations.
    """

self._on_ui_exit = on_ui_exit

self._command_handler_registry = (
    debugger_cli_common.CommandHandlerRegistry())

self._tab_completion_registry = debugger_cli_common.TabCompletionRegistry()

# Create top-level tab-completion context and register the exit and help
# commands.
self._tab_completion_registry.register_tab_comp_context(
    [""], self.CLI_EXIT_COMMANDS +
    [debugger_cli_common.CommandHandlerRegistry.HELP_COMMAND] +
    debugger_cli_common.CommandHandlerRegistry.HELP_COMMAND_ALIASES)

self._config = config or cli_config.CLIConfig()
self._config_argparser = argparse.ArgumentParser(
    description="config command", usage=argparse.SUPPRESS)
subparsers = self._config_argparser.add_subparsers()
set_parser = subparsers.add_parser("set")
set_parser.add_argument("property_name", type=str)
set_parser.add_argument("property_value", type=str)
set_parser = subparsers.add_parser("show")
self.register_command_handler(
    "config",
    self._config_command_handler,
    self._config_argparser.format_help(),
    prefix_aliases=["cfg"])
