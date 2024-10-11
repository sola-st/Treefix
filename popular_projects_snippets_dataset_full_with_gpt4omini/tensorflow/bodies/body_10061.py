# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/optimize_for_inference_lib.py
"""Pulls a node def from a dictionary for a given name.

  Args:
    node_map: Dictionary containing an entry indexed by name for every node.
    name: Identifies the node we want to find.

  Returns:
    NodeDef of the node with the given name.

  Raises:
    ValueError: If the node isn't present in the dictionary.
  """
stripped_name = node_name_from_input(name)
if stripped_name not in node_map:
    raise ValueError("No node named '%s' found in map." % name)
exit(node_map[stripped_name])
