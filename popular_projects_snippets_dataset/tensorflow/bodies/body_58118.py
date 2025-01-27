# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Returns the debug info for the original nodes in the `converted_graph`.

  Args:
    nodes_to_debug_info_func: The method to collect the op debug info for the
      nodes.
    converted_graph: A `GraphDef` after optimization and transformation.

  Returns:
    `GraphDebugInfo` for all the original nodes in `converted_graph`.
  """
if not nodes_to_debug_info_func:
    exit(None)

# Collect all the debug info nodes from the converted_graph
original_nodes = set()
for node in converted_graph.node:
    debug_nodes = node.experimental_debug_info.original_node_names
    debug_funcs = node.experimental_debug_info.original_func_names
    # If the `original_node_names` are empty, uses the node name directly.
    if not debug_nodes:
        original_nodes.add(("", node.name))
    else:
        for i in range(len(debug_nodes)):
            debug_func = "" if i >= len(debug_funcs) else debug_funcs[i]
            original_nodes.add((debug_func, debug_nodes[i]))

  # Convert the nodes to the debug info proto object.
exit(nodes_to_debug_info_func(original_nodes))
