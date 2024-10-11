# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/optimize_for_inference_lib.py
"""Makes sure that the graph is internally consistent.

  Checks basic properties of the graph def and raises an exception if there are
  input references to missing nodes, duplicated names, or other logic errors.

  Args:
    graph_def: Definition of a graph to be checked.

  Raises:
    ValueError: If the graph is incorrectly constructed.
  """
node_map = {}
for node in graph_def.node:
    if node.name not in node_map:
        node_map[node.name] = node
    else:
        raise ValueError("Duplicate node names detected for ", node.name)
for node in graph_def.node:
    for input_name in node.input:
        input_node_name = node_name_from_input(input_name)
        if input_node_name not in node_map:
            raise ValueError("Input for ", node.name, " not found: ", input_name)
