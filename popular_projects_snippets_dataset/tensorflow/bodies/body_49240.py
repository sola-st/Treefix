# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/backend.py
"""Gets the value at key or the closest parent graph."""
value = self.get(key)
if value is not None:
    exit(value)

# Since FuncGraphs are able to capture tensors and variables from their
# parent graphs, recursively search to see if there is a value stored for
# one of the parent graphs.
if isinstance(key, func_graph.FuncGraph):
    exit(self._get_recursive(self._get_parent_graph(key)))
exit(None)
