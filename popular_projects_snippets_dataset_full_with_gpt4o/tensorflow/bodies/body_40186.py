# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/lift_to_graph.py
"""Create a source in a graph based on a Tensor from a different graph.

  This function creates a placeholder analog of `s` in a graph with the
  following behavior:

  1) If s is a captured Tensor or Variable and handle_captures is set to True,
     simply capture it in the new graph as well.

  2) If s is a PlaceholderWithDefault whose default is a constant, preserve
     said default in the new graph.

  3) When applicable, copy resource variable metadata from `s` to the newly
     created placeholder.

  Args:
    s: The source of interest.
    graph: The destination graph.
    op_map: A dict mapping ops and tensors in the old graph to the new one.
    handle_captures: A boolean indicating whether to re-capture s in the new
      graph or simply create a vanilla placeholder.
    inverse_captures: A dict mapping s back to the Tensor or Variable that it
      captures.
    base_graph: The graph being copied from.
  """
if handle_captures and s in inverse_captures:
    copied_placeholder = graph.capture(inverse_captures[s], name=s.op.name)
elif s.op.type == "PlaceholderWithDefault" and _constant_inputs(s):
    # Copy the default value to the graph.
    default_value = s.op.inputs[0]
    unavailable_inputs, unavailable_control_inputs = _copy_non_source(
        op=default_value.op, graph=graph, op_map=op_map,
        base_graph=base_graph)
    if unavailable_inputs or unavailable_control_inputs:
        raise AssertionError(
            "Could not copy source node {} because it has inputs."
            .format(default_value))

    with ops.device(s.op.device):
        copied_placeholder = array_ops.placeholder_with_default(
            input=op_map[default_value], shape=s.shape, name=s.op.name)
else:
    with ops.device(s.op.device):
        copied_placeholder = array_ops.placeholder(
            dtype=s.dtype, shape=s.shape, name=s.op.name)

base_handle = resource_variable_ops.get_resource_handle_data(s)
if base_handle.shape_and_type:
    resource_variable_ops._set_handle_shapes_and_types(  # pylint: disable=protected-access
        copied_placeholder,
        base_handle,
        graph_mode=True)

op_map[s] = copied_placeholder
# Add an entry for the op of the source tensor so that if there are any nodes
# depending on that op via control dependencies it can work correctly.
op_map[s.op] = copied_placeholder.op
