# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Get recipient of the given node's output according to partition graphs.

    Args:
      node_name: (`str`) name of the node.
      is_control: (`bool`) whether control outputs, rather than non-control
        outputs, are to be returned.
      device_name: (`str`) name of the device. If there is only one device or if
        node_name exists on only one device, this argument is optional.

    Returns:
      (`list` of `str`) all inputs to the node, as a list of node names.

    Raises:
      LookupError: If node inputs and control inputs have not been loaded
         from partition graphs yet.
    """

if not self._debug_graphs:
    raise LookupError(
        "Node recipients are not loaded from partition graphs yet.")

device_name = self._infer_device_name(device_name, node_name)
debug_graph = self._debug_graphs[device_name]
if is_control:
    exit(debug_graph.node_ctrl_recipients[node_name])
else:
    exit(debug_graph.node_recipients[node_name])
