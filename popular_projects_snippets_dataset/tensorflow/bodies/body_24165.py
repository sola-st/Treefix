# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/hooks.py
if not self._session_wrapper:
    self._session_wrapper = local_cli_wrapper.LocalCLIDebugWrapperSession(
        run_context.session,
        ui_type=self._ui_type,
        dump_root=self._dump_root,
        thread_name_filter=self._thread_name_filter,
        config_file_path=self._config_file_path)

    # Actually register tensor filters registered prior to the construction
    # of the underlying LocalCLIDebugWrapperSession object.
    for filter_name in self._pending_tensor_filters:
        self._session_wrapper.add_tensor_filter(
            filter_name, self._pending_tensor_filters[filter_name])

    # Increment run call counter.
self._session_wrapper.increment_run_call_count()

# Adapt run_context to an instance of OnRunStartRequest for invoking
# superclass on_run_start().
on_run_start_request = framework.OnRunStartRequest(
    run_context.original_args.fetches, run_context.original_args.feed_dict,
    None, None, self._session_wrapper.run_call_count)

on_run_start_response = self._session_wrapper.on_run_start(
    on_run_start_request)
self._performed_action = on_run_start_response.action

run_args = session_run_hook.SessionRunArgs(
    None, feed_dict=None, options=config_pb2.RunOptions())
if self._performed_action == framework.OnRunStartAction.DEBUG_RUN:
    # pylint: disable=protected-access
    self._session_wrapper._decorate_run_options_for_debug(
        run_args.options,
        on_run_start_response.debug_urls,
        debug_ops=on_run_start_response.debug_ops,
        node_name_regex_allowlist=(
            on_run_start_response.node_name_regex_allowlist),
        op_type_regex_allowlist=(
            on_run_start_response.op_type_regex_allowlist),
        tensor_dtype_regex_allowlist=(
            on_run_start_response.tensor_dtype_regex_allowlist),
        tolerate_debug_op_creation_failures=(
            on_run_start_response.tolerate_debug_op_creation_failures))
    # pylint: enable=protected-access
elif self._performed_action == framework.OnRunStartAction.PROFILE_RUN:
    # pylint: disable=protected-access
    self._session_wrapper._decorate_run_options_for_profile(run_args.options)
    # pylint: enable=protected-access

exit(run_args)
