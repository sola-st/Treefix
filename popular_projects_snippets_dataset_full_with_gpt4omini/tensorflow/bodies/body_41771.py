# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
self._detectors = weakref.WeakKeyDictionary()  # GUARDED_BY(self._lock)
self._lock = threading.Lock()
