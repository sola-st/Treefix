# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator.py
"""Create a LooperThread.

    Args:
      coord: A Coordinator.
      timer_interval_secs: Time boundaries at which to call Run(), or None
        if it should be called back to back.
      target: Optional callable object that will be executed in the thread.
      args: Optional arguments to pass to `target` when calling it.
      kwargs: Optional keyword arguments to pass to `target` when calling it.

    Raises:
      ValueError: If one of the arguments is invalid.
    """
if not isinstance(coord, Coordinator):
    raise ValueError("'coord' argument must be a Coordinator: %s" % coord)
super(LooperThread, self).__init__()
self.daemon = True
self._coord = coord
self._timer_interval_secs = timer_interval_secs
self._target = target
if self._target:
    self._args = args or ()
    self._kwargs = kwargs or {}
elif args or kwargs:
    raise ValueError("'args' and 'kwargs' argument require that you also "
                     "pass 'target'")
self._coord.register_thread(self)
