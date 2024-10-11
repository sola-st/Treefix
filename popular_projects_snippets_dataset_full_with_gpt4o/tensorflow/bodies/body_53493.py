# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Adds 'op' to the graph and returns the unique ID for the added Operation.

    Args:
      op: the Operation to add.
      op_name: the name of the Operation.

    Returns:
      An integer that is a unique ID for the added Operation.
    """
self._check_not_finalized()
with self._lock:
    self._next_id_counter += 1
    op_id = self._next_id_counter
    self._nodes_by_id[op_id] = op
    self._nodes_by_name[op_name] = op
    self._version = max(self._version, op_id)
    exit(op_id)
