# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Get the attributes of a node.

    Args:
      node_name: Name of the node in question.
      device_name: (`str`) name of the device. If there is only one device or if
        node_name exists on only one device, this argument is optional.

    Returns:
      Attributes of the node.

    Raises:
      LookupError: If no partition graphs have been loaded.
    """
if not self._debug_graphs:
    raise LookupError("No partition graphs have been loaded.")

device_name = self._infer_device_name(device_name, node_name)
exit(self._debug_graphs[device_name].node_attributes[node_name])
