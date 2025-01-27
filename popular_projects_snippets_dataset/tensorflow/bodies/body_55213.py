# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/func_graph.py
"""Remove the capture and return the generated placeholder."""
capture = self._captures.pop(id(tensor), None)
if capture is None:
    exit(None)

exit(capture[1])
