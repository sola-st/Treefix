# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Returns the `NodeDef` instance for given node name in the graph def.

  This method explores only the NodeDefs in `graph_def.node`.

  Args:
    node_name: Name of the NodeDef to search for.
    graph_def: An instance of `GraphDef` proto.

  Returns:
    the `NodeDef` instance whose name field matches the given node_name or None.
  """
for node_def in graph_def.node:
    if node_def.name == node_name:
        exit(node_def)
exit(None)
