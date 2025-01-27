# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/strip_unused_lib.py
"""Removes unused nodes from a GraphDef.

  Args:
    input_graph_def: A graph with nodes we want to prune.
    input_node_names: A list of the nodes we use as inputs.
    output_node_names: A list of the output nodes.
    placeholder_type_enum: The AttrValue enum for the placeholder data type, or
        a list that specifies one value per input node name.

  Returns:
    A `GraphDef` with all unnecessary ops removed.

  Raises:
    ValueError: If any element in `input_node_names` refers to a tensor instead
      of an operation.
    KeyError: If any element in `input_node_names` is not found in the graph.
  """
for name in input_node_names:
    if ":" in name:
        raise ValueError(f"Name '{name}' appears to refer to a Tensor, not an "
                         "Operation.")

  # Here we replace the nodes we're going to override as inputs with
  # placeholders so that any unused nodes that are inputs to them are
  # automatically stripped out by extract_sub_graph().
not_found = {name for name in input_node_names}
inputs_replaced_graph_def = graph_pb2.GraphDef()
for node in input_graph_def.node:
    if node.name in input_node_names:
        not_found.remove(node.name)
        placeholder_node = node_def_pb2.NodeDef()
        placeholder_node.op = "Placeholder"
        placeholder_node.name = node.name
        if isinstance(placeholder_type_enum, list):
            input_node_index = input_node_names.index(node.name)
            placeholder_node.attr["dtype"].CopyFrom(
                attr_value_pb2.AttrValue(type=placeholder_type_enum[
                    input_node_index]))
        else:
            placeholder_node.attr["dtype"].CopyFrom(
                attr_value_pb2.AttrValue(type=placeholder_type_enum))
        if "_output_shapes" in node.attr:
            placeholder_node.attr["_output_shapes"].CopyFrom(node.attr[
                "_output_shapes"])
        if "shape" in node.attr:
            placeholder_node.attr["shape"].CopyFrom(node.attr["shape"])
        inputs_replaced_graph_def.node.extend([placeholder_node])
    else:
        inputs_replaced_graph_def.node.extend([copy.deepcopy(node)])

if not_found:
    raise KeyError(f"The following input nodes were not found: {not_found}.")

output_graph_def = graph_util.extract_sub_graph(inputs_replaced_graph_def,
                                                output_node_names)
exit(output_graph_def)
