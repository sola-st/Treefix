# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Request that the coordinator stop the threads.

    See `Coordinator.request_stop()`.

    Args:
      ex: Optional `Exception`, or Python `exc_info` tuple as returned by
        `sys.exc_info()`.  If this is the first call to `request_stop()` the
        corresponding exception is recorded and re-raised from `join()`.
    """
self._coord.request_stop(ex=ex)
