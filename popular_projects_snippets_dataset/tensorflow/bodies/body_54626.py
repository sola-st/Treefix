# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
for n in self._nodes.values():
    n.create_edges()
