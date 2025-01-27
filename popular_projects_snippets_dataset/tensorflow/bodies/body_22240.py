# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Context handler to stop the supervisor when an exception is raised.

    See `Coordinator.stop_on_exception()`.

    Returns:
      A context handler.
    """
exit(self._coord.stop_on_exception())
