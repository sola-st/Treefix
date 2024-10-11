# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
self._checkpoint = checkpoint
self._object_graph_view = object_graph_view
self._optionally_restored = []
# Keep a reference to the root, since graph_view might only have a weakref.
self._root = object_graph_view.root
