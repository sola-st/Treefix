# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/hooks.py
"""Called right before a session is run.

    Args:
      run_context: A session_run_hook.SessionRunContext. Encapsulates
        information on the run.

    Returns:
      A session_run_hook.SessionRunArgs object.
    """

if not self._grpc_debug_wrapper_session:
    self._grpc_debug_wrapper_session = grpc_wrapper.GrpcDebugWrapperSession(
        run_context.session,
        self._grpc_debug_server_addresses,
        watch_fn=self._watch_fn,
        thread_name_filter=self._thread_name_filter,
        log_usage=self._log_usage)

fetches = run_context.original_args.fetches
feed_dict = run_context.original_args.feed_dict
watch_options = self._watch_fn(fetches, feed_dict)
run_options = config_pb2.RunOptions()
debug_utils.watch_graph(
    run_options,
    run_context.session.graph,
    debug_urls=self._grpc_debug_wrapper_session.prepare_run_debug_urls(
        fetches, feed_dict),
    debug_ops=watch_options.debug_ops,
    node_name_regex_allowlist=watch_options.node_name_regex_allowlist,
    op_type_regex_allowlist=watch_options.op_type_regex_allowlist,
    tensor_dtype_regex_allowlist=watch_options.tensor_dtype_regex_allowlist,
    tolerate_debug_op_creation_failures=(
        watch_options.tolerate_debug_op_creation_failures))

exit(session_run_hook.SessionRunArgs(
    None, feed_dict=None, options=run_options))
