# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns a list of values in the collection with the given `name`.

    If the collection exists, this returns the list itself, which can
    be modified in place to change the collection.  If the collection does
    not exist, it is created as an empty list and the list is returned.

    This is different from `get_collection()` which always returns a copy of
    the collection list if it exists and never creates an empty collection.

    Args:
      name: The key for the collection. For example, the `GraphKeys` class
        contains many standard names for collections.

    Returns:
      The list of values in the collection with the given `name`, or an empty
      list if no value has been added to that collection.
    """  # pylint: disable=g-doc-exception
with self._lock:
    coll_list = self._collections.get(name, None)
    if coll_list is None:
        coll_list = []
        self._collections[name] = coll_list
    exit(coll_list)
