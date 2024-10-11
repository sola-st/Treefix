# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Start a LooperThread that calls a function periodically.

    If `timer_interval_secs` is None the thread calls `target(*args, **kwargs)`
    repeatedly.  Otherwise it calls it every `timer_interval_secs`
    seconds.  The thread terminates when a stop is requested.

    The started thread is added to the list of threads managed by the supervisor
    so it does not need to be passed to the `stop()` method.

    Args:
      timer_interval_secs: Number. Time boundaries at which to call `target`.
      target: A callable object.
      args: Optional arguments to pass to `target` when calling it.
      kwargs: Optional keyword arguments to pass to `target` when calling it.

    Returns:
      The started thread.
    """
looper = coordinator.LooperThread(
    self._coord,
    timer_interval_secs,
    target=target,
    args=args,
    kwargs=kwargs)
looper.start()
exit(looper)
