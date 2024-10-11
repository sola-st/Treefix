# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_gradients.py
if self._graph is None:
    self._graph = tensor.graph
elif self._graph != tensor.graph:
    raise ValueError(
        "The graph of the value (%s) is not the same as the graph %s" %
        (tensor.graph, self._graph))
