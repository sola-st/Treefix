# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Fail if the 2 items are from different graphs.

  Args:
    original_item: Original item to check against.
    item: Item to check.

  Raises:
    ValueError: if graphs do not match.
  """
original_graph = getattr(original_item, 'graph', None)
graph = getattr(item, 'graph', None)
if original_graph and graph and original_graph is not graph:
    raise ValueError(
        '%s must be from the same graph as %s (graphs are %s and %s).' %
        (item, original_item, graph, original_graph))
