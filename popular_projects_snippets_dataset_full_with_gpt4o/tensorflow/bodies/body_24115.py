# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework.py
"""Constructor of `OnRunStartRequest`.

    Args:
      fetches: Fetch targets of the run() call.
      feed_dict: The feed dictionary to the run() call.
      run_options: RunOptions input to the run() call.
      run_metadata: RunMetadata input to the run() call.
        The above four arguments are identical to the input arguments to the
        run() method of a non-wrapped TensorFlow session.
      run_call_count: 1-based count of how many run calls (including this one)
        has been invoked.
      is_callable_runner: (bool) whether a runner returned by
        Session.make_callable is being run.
    """
self.fetches = fetches
self.feed_dict = feed_dict
self.run_options = run_options
self.run_metadata = run_metadata
self.run_call_count = run_call_count
self.is_callable_runner = is_callable_runner
