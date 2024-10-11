# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Set the captures with the provided list of captures & placeholder."""
self._captures = py_collections.OrderedDict()
for tensor, placeholder in capture_list:
    self._captures[id(tensor)] = (tensor, placeholder)
