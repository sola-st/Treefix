# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper.py
"""Update the internal state with regard to run() call history.

    Args:
      run_call_count: (int) Number of run() calls that have occurred.
      fetches: a node/tensor or a list of node/tensor that are the fetches of
        the run() call. This is the same as the fetches argument to the run()
        call.
      feed_dict: None of a dict. This is the feed_dict argument to the run()
        call.
      is_callable_runner: (bool) whether a runner returned by
        Session.make_callable is being run.
    """

self._run_call_count = run_call_count
self._feed_dict = feed_dict
self._run_description = cli_shared.get_run_short_description(
    run_call_count,
    fetches,
    feed_dict,
    is_callable_runner=is_callable_runner)
self._run_through_times -= 1

self._run_info = cli_shared.get_run_start_intro(
    run_call_count,
    fetches,
    feed_dict,
    self._tensor_filters,
    is_callable_runner=is_callable_runner)
