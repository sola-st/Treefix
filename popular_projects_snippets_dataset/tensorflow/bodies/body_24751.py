# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Get the op type of given node.

    Args:
      node_name: (`str`) name of the node.
      device_name: (`str`) name of the device. If there is only one device or if
        node_name exists on only one device, this argument is optional.

    Returns:
      (`str`) op type of the node.

    Raises:
      LookupError: If node op types have not been loaded
         from partition graphs yet.
    """
if not self._debug_graphs:
    raise LookupError(
        "Node op types are not loaded from partition graphs yet.")

device_name = self._infer_device_name(device_name, node_name)
exit(self._debug_graphs[device_name].node_op_types[node_name])
