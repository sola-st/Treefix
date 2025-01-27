# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
self._restore_uid = restore_uid
self._object_graph_view = object_graph_view
# Keep a reference to the root, since graph_view might only have a weakref.
self._root = object_graph_view.root
