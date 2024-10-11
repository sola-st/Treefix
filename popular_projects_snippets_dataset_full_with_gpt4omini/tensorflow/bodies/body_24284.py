# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper.py
"""Command handler for "run" command during on-run-start."""

del screen_info  # Currently unused.

parsed = self._argparsers["run"].parse_args(args)
parsed.node_name_filter = parsed.node_name_filter or None
parsed.op_type_filter = parsed.op_type_filter or None
parsed.tensor_dtype_filter = parsed.tensor_dtype_filter or None

if parsed.filter_exclude_node_names and not parsed.till_filter_pass:
    raise ValueError(
        "The --filter_exclude_node_names (or -feon) flag is valid only if "
        "the --till_filter_pass (or -f) flag is used.")

if parsed.profile:
    raise debugger_cli_common.CommandLineExit(
        exit_token=framework.OnRunStartResponse(
            framework.OnRunStartAction.PROFILE_RUN, []))

self._skip_debug = parsed.no_debug
self._run_through_times = parsed.times

if parsed.times > 1 or parsed.no_debug:
    # If requested -t times > 1, the very next run will be a non-debug run.
    action = framework.OnRunStartAction.NON_DEBUG_RUN
    debug_urls = []
else:
    action = framework.OnRunStartAction.DEBUG_RUN
    debug_urls = self._get_run_debug_urls()
run_start_response = framework.OnRunStartResponse(
    action,
    debug_urls,
    node_name_regex_allowlist=parsed.node_name_filter,
    op_type_regex_allowlist=parsed.op_type_filter,
    tensor_dtype_regex_allowlist=parsed.tensor_dtype_filter)

if parsed.till_filter_pass:
    # For the run-till-filter-pass (run -f) mode, use the DEBUG_RUN
    # option to access the intermediate tensors, and set the corresponding
    # state flag of the class itself to True.
    if parsed.till_filter_pass in self._tensor_filters:
        action = framework.OnRunStartAction.DEBUG_RUN
        self._active_tensor_filter = parsed.till_filter_pass
        self._active_filter_exclude_node_names = (
            parsed.filter_exclude_node_names)
        self._active_tensor_filter_run_start_response = run_start_response
    else:
        # Handle invalid filter name.
        exit(debugger_cli_common.RichTextLines(
            ["ERROR: tensor filter \"%s\" does not exist." %
             parsed.till_filter_pass]))

    # Raise CommandLineExit exception to cause the CLI to exit.
raise debugger_cli_common.CommandLineExit(exit_token=run_start_response)
