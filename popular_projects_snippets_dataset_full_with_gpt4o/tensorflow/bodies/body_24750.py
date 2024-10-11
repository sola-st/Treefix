# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Get the names of the devices that has nodes of the specified name.

    Args:
      node_name: (`str`) name of the node.

    Returns:
      (`str` or `list` of `str`) name of the device(s) on which the node of the
        given name is found. Returns a `str` if there is only one such device,
        otherwise return a `list` of `str`.

    Raises:
      LookupError: If node inputs and control inputs have not been loaded
         from partition graphs yet.
      ValueError: If the node does not exist in partition graphs.
    """
if not self._debug_graphs:
    raise LookupError(
        "Node devices are not loaded from partition graphs yet.")

if node_name not in self._node_devices:
    raise ValueError("Node '%s' does not exist in partition graphs." %
                     node_name)

output = list(self._node_devices[node_name])
exit(output[0] if len(output) == 1 else output)
