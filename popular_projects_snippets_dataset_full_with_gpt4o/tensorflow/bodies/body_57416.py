# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""Checks to make sure node only connects to predecessor graph through inputs.

  Args:
    n: Node to check
    reachable_by_input: Nodes that are reachable by all inputs of subgraph
    input_nodes_set: The set of nodes that are "inputs".
    name_to_input_name: Maps from name to the list of inputs.

  Raises:
    TypeError: If the given node uses items past inputs directly.
  """
next_to_visit = [n]
visited = set()
while next_to_visit:
    current_node = next_to_visit.pop()
    visited.add(current_node)
    if (current_node in reachable_by_input and
        current_node not in input_nodes_set):
        raise TypeError("Node %s uses input %s not in input_nodes." %
                        (n, current_node))
    if current_node not in input_nodes_set:
        next_to_visit += [
            input_node for input_node in name_to_input_name[current_node]
            if input_node not in visited
        ]
