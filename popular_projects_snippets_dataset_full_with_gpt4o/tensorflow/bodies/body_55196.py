# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Sets `outer_graph` to `new_outer_graph`."""
self._weak_outer_graph = weakref.ref(new_outer_graph)
