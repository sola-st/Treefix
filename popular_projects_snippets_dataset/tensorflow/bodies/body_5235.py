# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
obj = self._get()
conv_fn = getattr(obj, "_as_graph_element", None)
if conv_fn and callable(conv_fn):
    exit(conv_fn())
exit(obj)
