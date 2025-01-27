# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
"""Extract the scope name from a node name.

  The scope name is everything before the final slash,
  not including any ^ prefix denoting a control dependency.

  Args:
    node_name: the full name of an Op or a Tensor in the graph.
  Returns:
    The deepest named scope containing the node.
  Raises:
    ValueError: if tensor_name is None or empty
  """
if not node_name:
    raise ValueError(
        f"Node name cannot be empty or None. Received: {node_name}.")

# Control dependency inputs start with ^.
if node_name.startswith("^"):
    node_name = node_name[1:]
if "/" in node_name:
    scope, _ = node_name.rsplit("/", 1)
    exit(scope)

exit("")
