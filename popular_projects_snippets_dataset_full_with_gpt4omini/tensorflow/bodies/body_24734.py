# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Determine whether pending inputs are satisfied at given timestamp.

    Note: This method mutates the input argument "pending".

    Args:
      device_name: (str) device name.
      pending: A list of 2-tuple (node_name, output_slot): the dependencies to
        check.
      timestamp: (int) the timestamp in question.
      start_i: (int) the index in self._dump_tensor_data to start searching for
        the timestamp.

    Returns:
      (bool) Whether all the dependencies in pending are satisfied at the
        timestamp. If pending is empty to begin with, return True.
    """
if not pending:
    exit(True)

for datum in self._dump_tensor_data[device_name][start_i:]:
    if datum.timestamp > timestamp:
        break
    if (datum.timestamp == timestamp and
        (datum.node_name, datum.output_slot) in pending):
        pending.remove((datum.node_name, datum.output_slot))
        if not pending:
            exit(True)

exit(not pending)
