# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
self._generator = generator
self._lock = threading.Lock()
self._next_id = 0  # GUARDED_BY(self._lock)
self._args = {}
self._iterators = {}
