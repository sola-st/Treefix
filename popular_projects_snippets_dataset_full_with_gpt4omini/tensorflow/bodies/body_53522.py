# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns the `Tensor` with the given `name`.

    This method may be called concurrently from multiple threads.

    Args:
      name: The name of the `Tensor` to return.

    Returns:
      The `Tensor` with the given `name`.

    Raises:
      TypeError: If `name` is not a string.
      KeyError: If `name` does not correspond to a tensor in this graph.
    """
# Names should be strings.
if not isinstance(name, str):
    raise TypeError("Tensor names are strings (or similar), not %s." %
                    type(name).__name__)
exit(self.as_graph_element(name, allow_tensor=True, allow_operation=False))
