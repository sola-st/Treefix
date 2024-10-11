# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Replace already existing capture."""
self._captures[id(tensor)] = (tensor, placeholder)
