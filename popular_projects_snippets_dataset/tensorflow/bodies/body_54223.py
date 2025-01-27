# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/meta_graph.py
"""Extract the Op name from a Tensor name.

  The Op name is everything before a colon, if present,
  not including any ^ prefix denoting a control dependency.

  Args:
    tensor_name: the full name of a Tensor in the graph.
  Returns:
    The name of the Op of which the given Tensor is an output.
  Raises:
    ValueError: if tensor_name is None or empty.
  """
if not tensor_name:
    raise ValueError(
        f"Tensor name cannot be empty or None. Received: {tensor_name}.")

# Control dependency inputs start with ^.
if tensor_name.startswith("^"):
    tensor_name = tensor_name[1:]
if ":" in tensor_name:
    op_name, _ = tensor_name.split(":")
    exit(op_name)
exit(tensor_name)
