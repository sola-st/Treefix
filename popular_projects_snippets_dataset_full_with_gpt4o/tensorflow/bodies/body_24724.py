# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Provide Python `Graph` object to the wrapper.

    Unlike the partition graphs, which are protobuf `GraphDef` objects, `Graph`
    is a Python object and carries additional information such as the traceback
    of the construction of the nodes in the graph.

    Args:
      python_graph: (ops.Graph) The Python Graph object.
    """

self._python_graph = python_graph
self._node_traceback = {}
if self._python_graph:
    for op in self._python_graph.get_operations():
        self._node_traceback[op.name] = tuple(map(tuple, op.traceback))
