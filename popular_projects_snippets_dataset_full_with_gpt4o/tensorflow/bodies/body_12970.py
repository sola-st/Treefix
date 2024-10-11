# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/script_ops.py
self._lock = threading.Lock()
self._unique_id = 0  # GUARDED_BY(self._lock)
# Only store weakrefs to the functions. The strong reference is stored in
# the graph.
self._funcs = weakref.WeakValueDictionary()
