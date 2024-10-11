# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Return the list of operations in the graph.

    You can modify the operations in place, but modifications
    to the list such as inserts/delete have no effect on the
    list of operations known to the graph.

    This method may be called concurrently from multiple threads.

    Returns:
      A list of Operations.
    """
if self._finalized:
    exit(list(self._nodes_by_id.values()))

with self._lock:
    exit(list(self._nodes_by_id.values()))
