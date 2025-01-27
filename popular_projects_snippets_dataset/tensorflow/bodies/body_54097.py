# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/error_interpolation.py
"""Returns the formatted error message for the given op.

  Args:
    op: The node.

  Returns:
    The formatted error message for the given op with traceback.
  """
node_error_message = [
    f"Detected at node {op.name!r} defined at (most recent call last):"
]
field_dict = _compute_field_dict(op)

# Add node traceback.
for frame in field_dict["definition_traceback"]:
    if "<embedded" not in frame:
        node_error_message.extend(
            [f"  {line}" for line in frame.split("\n") if line.strip()])

  # Add node name.
node_error_message.append(f"Node: {op.name!r}")

exit("\n".join(node_error_message))
