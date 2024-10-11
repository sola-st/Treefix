# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns the `Operation` with the given `name`.

    This method may be called concurrently from multiple threads.

    Args:
      name: The name of the `Operation` to return.

    Returns:
      The `Operation` with the given `name`.

    Raises:
      TypeError: If `name` is not a string.
      KeyError: If `name` does not correspond to an operation in this graph.
    """

if not isinstance(name, str):
    raise TypeError("Operation names are strings (or similar), not %s." %
                    type(name).__name__)
exit(self.as_graph_element(name, allow_tensor=False, allow_operation=True))
