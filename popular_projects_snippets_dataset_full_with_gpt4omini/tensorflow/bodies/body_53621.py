# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Cleans up reference cycles from a `Graph`.

  Helpful for making sure the garbage collector doesn't need to run after a
  temporary `Graph` is no longer needed.

  Args:
    graph: A `Graph` object to destroy. Neither it nor any of its ops are usable
      after this function runs.
  """
graph._functions.clear()  # pylint: disable=protected-access

# Now clean up Operation<->Graph reference cycles by clearing all of the
# attributes for the Graph and its ops.
graph_operations = graph.get_operations()
for op in graph_operations:
    op.__dict__ = {}
graph.__dict__ = {}
