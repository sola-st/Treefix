# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Annotates variable operations with custom `_shape` attribute.

  This is required for the converters and shape inference. The graph
  definition is modified in-place.

  Args:
    func: Function represented by the graph definition.
    graph_def: Graph definition to be annotated in-place.

  Raises:
    RuntimeError: if some shapes cannot be annotated.
  """
ph_shape_map = {}
for ph, var in zip(func.graph.internal_captures, func.variables):
    ph_shape_map[ph.name] = var.shape
# Construct a mapping of node names to nodes
name_to_node = {node.name: node for node in graph_def.node}
# Go through all the ReadVariableOp nodes in the graph def
for node in graph_def.node:
    if node.op == "ReadVariableOp" or node.op == "ResourceGather":
        node_ = node
        # Go up the chain of identities to find a placeholder
        while name_to_node[node_.input[0]].op == "Identity":
            node_ = name_to_node[node_.input[0]]
        ph_name = node_.input[0] + ":0"
        if ph_name in ph_shape_map:
            shape = ph_shape_map[ph_name]
            node.attr["_shape"].shape.CopyFrom(shape.as_proto())
        else:
            raise RuntimeError(
                "Not found in the function captures: {}".format(ph_name))
