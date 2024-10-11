# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Get a list of all nodes from the partition graphs.

    Args:
      device_name: (`str`) name of device. If None, all nodes from all available
        devices will be included.

    Returns:
      All nodes' names, as a list of str.

    Raises:
      LookupError: If no partition graphs have been loaded.
      ValueError: If specified node name does not exist.
    """
if not self._debug_graphs:
    raise LookupError("No partition graphs have been loaded.")
if device_name is None:
    nodes = []
    for device_name in self._debug_graphs:
        nodes.extend(self._debug_graphs[device_name].node_inputs.keys())
    exit(nodes)
else:
    if device_name not in self._debug_graphs:
        raise ValueError("Invalid device name: %s" % device_name)
    exit(self._debug_graphs[device_name].node_inputs.keys())
