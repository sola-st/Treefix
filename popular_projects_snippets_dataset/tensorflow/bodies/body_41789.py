# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Restore from pickled state."""
self.__dict__ = state
self._lock = threading.RLock()
self._descriptor_cache = weakref.WeakKeyDictionary()
self._key_for_call_stats = self._get_key_for_call_stats()
