# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/api.py
"""Asserts that the layout of the DTensor is `layout`.

  Args:
    tensor: A DTensor whose layout is to be checked.
    layout: The `Layout` to compare against.

  Raises:
    ValueError: If the layout of `tensor` does not match the supplied `layout`.
  """
if fetch_layout(tensor) != layout:
    raise ValueError("Layout of tensor: " + str(fetch_layout(tensor)) +
                     ", did not match expected layout: " + str(layout))
