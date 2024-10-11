# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Check if the specified tensor has been captured."""
exit(id(tensor) in self._captures)
