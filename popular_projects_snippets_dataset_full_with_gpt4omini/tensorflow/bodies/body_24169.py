# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/hooks.py
reset_disk_byte_usage = False
if not self._session_wrapper:
    self._session_wrapper = dumping_wrapper.DumpingDebugWrapperSession(
        run_context.session,
        self._session_root,
        watch_fn=self._watch_fn,
        thread_name_filter=self._thread_name_filter,
        log_usage=self._log_usage)
    reset_disk_byte_usage = True

self._session_wrapper.increment_run_call_count()

# pylint: disable=protected-access
debug_urls, watch_options = self._session_wrapper._prepare_run_watch_config(
    run_context.original_args.fetches, run_context.original_args.feed_dict)
# pylint: enable=protected-access
run_options = config_pb2.RunOptions()
debug_utils.watch_graph(
    run_options,
    run_context.session.graph,
    debug_urls=debug_urls,
    debug_ops=watch_options.debug_ops,
    node_name_regex_allowlist=watch_options.node_name_regex_allowlist,
    op_type_regex_allowlist=watch_options.op_type_regex_allowlist,
    tensor_dtype_regex_allowlist=watch_options.tensor_dtype_regex_allowlist,
    tolerate_debug_op_creation_failures=(
        watch_options.tolerate_debug_op_creation_failures),
    reset_disk_byte_usage=reset_disk_byte_usage)

run_args = session_run_hook.SessionRunArgs(
    None, feed_dict=None, options=run_options)
exit(run_args)
