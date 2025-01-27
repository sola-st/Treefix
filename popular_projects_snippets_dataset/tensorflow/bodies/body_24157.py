# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
"""See doc of BaseDebugWrapperSession.on_run_start."""

debug_urls, watch_opts = self._prepare_run_watch_config(
    request.fetches, request.feed_dict)

exit(OnRunStartResponse(
    OnRunStartAction.DEBUG_RUN,
    debug_urls,
    debug_ops=watch_opts.debug_ops,
    node_name_regex_allowlist=watch_opts.node_name_regex_allowlist,
    op_type_regex_allowlist=watch_opts.op_type_regex_allowlist,
    tensor_dtype_regex_allowlist=watch_opts.tensor_dtype_regex_allowlist,
    tolerate_debug_op_creation_failures=(
        watch_opts.tolerate_debug_op_creation_failures)))
