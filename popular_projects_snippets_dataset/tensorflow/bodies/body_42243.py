# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Remove an already-registered op callback.

    Args:
      callback: The op callback to be removed.

    Raises:
      KeyError: If `callback` is not already registered.
    """
if callback not in self._thread_local_data.op_callbacks:
    raise KeyError("The specified op callback has not been registered, "
                   "and hence cannot be removed.")
del self._thread_local_data.op_callbacks[
    self._thread_local_data.op_callbacks.index(callback)]
