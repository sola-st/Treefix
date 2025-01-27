# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Clears all values in a collection.

    Args:
      name: The key for the collection. The `GraphKeys` class contains many
        standard names for collections.
    """
self._check_not_finalized()
with self._lock:
    if name in self._collections:
        del self._collections[name]
