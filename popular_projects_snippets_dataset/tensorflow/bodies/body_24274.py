# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper.py
"""Overrides on-run-start callback.

    Args:
      request: An instance of `OnRunStartRequest`.

    Returns:
      An instance of `OnRunStartResponse`.
    """
self._is_run_start = True
self._update_run_calls_state(
    request.run_call_count, request.fetches, request.feed_dict,
    is_callable_runner=request.is_callable_runner)

if self._active_tensor_filter:
    # If we are running until a filter passes, we just need to keep running
    # with the previous `OnRunStartResponse`.
    exit(self._active_tensor_filter_run_start_response)

self._exit_if_requested_by_user()

if self._run_call_count > 1 and not self._skip_debug:
    if self._run_through_times > 0:
        # Just run through without debugging.
        exit(framework.OnRunStartResponse(
            framework.OnRunStartAction.NON_DEBUG_RUN, []))
    elif self._run_through_times == 0:
        # It is the run at which the run-end CLI will be launched: activate
        # debugging.
        exit((self._run_start_response or
                framework.OnRunStartResponse(
                    framework.OnRunStartAction.DEBUG_RUN,
                    self._get_run_debug_urls())))

if self._run_start_response is None:
    self._prep_cli_for_run_start()

    self._run_start_response = self._launch_cli()
    if self._active_tensor_filter:
        self._active_tensor_filter_run_start_response = self._run_start_response
    if self._run_through_times > 1:
        self._run_through_times -= 1

self._exit_if_requested_by_user()
exit(self._run_start_response)
