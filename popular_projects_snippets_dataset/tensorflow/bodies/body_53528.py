# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Stores `value` in the collection with the given `name`.

    Note that collections are not sets, so it is possible to add a value to
    a collection several times.

    Args:
      name: The key for the collection. The `GraphKeys` class contains many
        standard names for collections.
      value: The value to add to the collection.
    """  # pylint: disable=g-doc-exception
self._check_not_finalized()
with self._lock:
    if name not in self._collections:
        self._collections[name] = [value]
    else:
        self._collections[name].append(value)
