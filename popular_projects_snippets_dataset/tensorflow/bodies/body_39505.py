# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
self._checkpoint = checkpoint
self._feed_dict = feed_dict
self._object_graph_view = graph_view
# Keep a reference to the root, since object_graph_view might only have a
# weakref.
self._root = graph_view.root
