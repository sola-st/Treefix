# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Get the inputs of given node according to partition graphs.

    Args:
      node_name: Name of the node.
      is_control: (`bool`) Whether control inputs, rather than non-control
        inputs, are to be returned.
      device_name: (`str`) name of the device. If there is only one device or if
        node_name exists on only one device, this argument is optional.

    Returns:
      (`list` of `str`) inputs to the node, as a list of node names.

    Raises:
      LookupError: If node inputs and control inputs have not been loaded
         from partition graphs yet.
    """
if not self._debug_graphs:
    raise LookupError(
        "Node inputs are not loaded from partition graphs yet.")

device_name = self._infer_device_name(device_name, node_name)
if is_control:
    exit(self._debug_graphs[device_name].node_ctrl_inputs[node_name])
else:
    exit(self._debug_graphs[device_name].node_inputs[node_name])
