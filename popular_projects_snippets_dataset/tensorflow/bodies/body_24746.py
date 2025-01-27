# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Find a path between a source node and a destination node.

    Limitation: the source and destination are required to be on the same
    device, i.e., this method does not yet take into account Send/Recv nodes
    across devices.

    TODO(cais): Make this method work across device edges by tracing Send/Recv
      nodes.

    Args:
      src_node_name: (`str`) name of the source node or name of an output tensor
        of the node.
      dst_node_name: (`str`) name of the destination node or name of an output
        tensor of the node.
      include_control: (`bool`) whrther control edges are considered in the
        graph tracing.
      include_reversed_ref: Whether a ref input, say from A to B, is to be also
        considered as an input from B to A. The rationale is that ref inputs
        generally let the recipient (e.g., B in this case) mutate the value of
        the source (e.g., A in this case). So the reverse direction of the ref
        edge reflects the direction of information flow.
      device_name: (`str`) name of the device. If there is only one device or if
        node_name exists on only one device, this argument is optional.

    Returns:
      A path from the src_node_name to dst_node_name, as a `list` of `str`, if
      it exists. The list includes src_node_name as the first item and
      dst_node_name as the last.
      If such a path does not exist, `None`.

    Raises:
      ValueError: If the source and destination nodes are not on the same
        device.
    """
src_device_name = self._infer_device_name(device_name, src_node_name)
dst_device_name = self._infer_device_name(device_name, dst_node_name)

if src_device_name != dst_device_name:
    raise ValueError(
        "Source (%s) and destination (%s) are not on the same device: "
        "%s vs. %s" % (src_node_name, dst_node_name, src_device_name,
                       dst_device_name))

input_lists = [self._debug_graphs[dst_device_name].node_inputs]
debug_graph = self._debug_graphs[dst_device_name]
if include_control:
    input_lists.append(debug_graph.node_ctrl_inputs)
if include_reversed_ref:
    input_lists.append(debug_graph.node_reversed_ref_inputs)
tracer = debug_graphs.DFSGraphTracer(
    input_lists,
    skip_node_names=self._get_merge_node_names(dst_device_name),
    destination_node_name=src_node_name)
# Here the value of destination_node_name is src_node_name, because we
# are tracing the graph from output to its inputs (i.e., going backwards
# on the graph).

try:
    tracer.trace(dst_node_name)
except debug_graphs.GraphTracingReachedDestination:
    # Prune nodes not on the path.
    inputs = [dst_node_name] + tracer.inputs()
    depth_list = [0] + tracer.depth_list()

    path = []
    curr_depth = depth_list[-1]
    for inp, depth in zip(reversed(inputs), reversed(depth_list)):
        if depth == curr_depth:
            path.append(inp)
            curr_depth -= 1
    exit(path)
