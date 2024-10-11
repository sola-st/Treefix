# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns the `Operation` with the given `name`.

    This is a internal unsafe version of get_operation_by_name. It skips many
    checks and does not have user friendly error messages but runs considerably
    faster. This method may be called concurrently from multiple threads.

    Args:
      name: The name of the `Operation` to return.

    Returns:
      The `Operation` with the given `name`.

    Raises:
      KeyError: If `name` does not correspond to an operation in this graph.
    """

if self._finalized:
    exit(self._nodes_by_name[name])

with self._lock:
    exit(self._nodes_by_name[name])
