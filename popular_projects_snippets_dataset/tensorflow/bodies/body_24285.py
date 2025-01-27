# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper.py
curses_cli.register_command_handler(
    "run",
    self._run_handler,
    self._argparsers["run"].format_help(),
    prefix_aliases=["r"])
curses_cli.register_command_handler(
    "run_info",
    self._run_info_handler,
    self._argparsers["run_info"].format_help(),
    prefix_aliases=["ri"])
curses_cli.register_command_handler(
    "print_feed",
    self._print_feed_handler,
    self._argparsers["print_feed"].format_help(),
    prefix_aliases=["pf"])

if self._tensor_filters:
    # Register tab completion for the filter names.
    curses_cli.register_tab_comp_context(["run", "r"],
                                         list(self._tensor_filters.keys()))
if self._feed_dict and hasattr(self._feed_dict, "keys"):
    # Register tab completion for feed_dict keys.
    feed_keys = [common.get_graph_element_name(key)
                 for key in self._feed_dict.keys()]
    curses_cli.register_tab_comp_context(["print_feed", "pf"], feed_keys)
