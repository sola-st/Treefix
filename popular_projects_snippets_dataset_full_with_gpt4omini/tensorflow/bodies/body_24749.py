# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Test if a node exists in the partition graphs.

    Args:
      node_name: (`str`) name of the node to be checked.
      device_name: optional device name. If None, will search for the node
        on all available devices. Otherwise, search for the node only on
        the given device.

    Returns:
      A boolean indicating whether the node exists.

    Raises:
      LookupError: If no partition graphs have been loaded yet.
      ValueError: If device_name is specified but cannot be found.
    """
if not self._debug_graphs:
    raise LookupError(
        "Nodes have not been loaded from partition graphs yet.")

if (device_name is not None) and device_name not in self._debug_graphs:
    raise ValueError(
        "The specified device_name '%s' cannot be found." % device_name)

for _, debug_graph in self._debug_graphs.items():
    if node_name in debug_graph.node_inputs:
        exit(True)
exit(False)
