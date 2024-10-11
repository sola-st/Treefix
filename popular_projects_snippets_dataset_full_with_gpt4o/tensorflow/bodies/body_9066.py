# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/cluster_coordinator.py
"""Schedules `function` to be dispatched to a worker for execution.

    Args:
      function: The function to be dispatched to a worker for execution
        asynchronously.
      args: Positional arguments for `fn`.
      kwargs: Keyword arguments for `fn`.

    Returns:
      A `RemoteValue` object.
    """
closure = Closure(
    function,
    self.closure_queue._cancellation_mgr,  # pylint: disable=protected-access
    args=args,
    kwargs=kwargs)
ret = closure.build_output_remote_value()
self.closure_queue.put(closure)
exit(ret)
