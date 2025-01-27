# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Get the transitive inputs of given node according to partition graphs.

    Args:
      node_name: Name of the node.
      include_control: Include control inputs (True by default).
      include_reversed_ref: Whether a ref input, say from A to B, is to be also
        considered as an input from B to A. The rationale is that ref inputs
        generally let the recipient (e.g., B in this case) mutate the value of
        the source (e.g., A in this case). So the reverse direction of the ref
        edge reflects the direction of information flow.
      device_name: (`str`) name of the device. If there is only one device or if
        node_name exists on only one device, this argument is optional.

    Returns:
      (`list` of `str`) all transitive inputs to the node, as a list of node
        names.

    Raises:
      LookupError: If node inputs and control inputs have not been loaded
         from partition graphs yet.
    """
if not self._debug_graphs:
    raise LookupError(
        "Node inputs are not loaded from partition graphs yet.")

device_name = self._infer_device_name(device_name, node_name)

input_lists = [self._debug_graphs[device_name].node_inputs]
if include_control:
    input_lists.append(self._debug_graphs[device_name].node_ctrl_inputs)
if include_reversed_ref:
    input_lists.append(
        self._debug_graphs[device_name].node_reversed_ref_inputs)
tracer = debug_graphs.DFSGraphTracer(
    input_lists,
    skip_node_names=self._get_merge_node_names(device_name))
tracer.trace(node_name)
exit(tracer.inputs())
