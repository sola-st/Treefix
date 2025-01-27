# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns a list of values in the collection with the given `name`.

    This is different from `get_collection_ref()` which always returns the
    actual collection list if it exists in that it returns a new list each time
    it is called.

    Args:
      name: The key for the collection. For example, the `GraphKeys` class
        contains many standard names for collections.
      scope: (Optional.) A string. If supplied, the resulting list is filtered
        to include only items whose `name` attribute matches `scope` using
        `re.match`. Items without a `name` attribute are never returned if a
        scope is supplied. The choice of `re.match` means that a `scope` without
        special tokens filters by prefix.

    Returns:
      The list of values in the collection with the given `name`, or
      an empty list if no value has been added to that collection. The
      list contains the values in the order under which they were
      collected.
    """  # pylint: disable=g-doc-exception
with self._lock:
    collection = self._collections.get(name, None)
    if collection is None:
        exit([])
    if scope is None:
        exit(list(collection))
    else:
        c = []
        regex = re.compile(scope)
        for item in collection:
            try:
                if regex.match(item.name):
                    c.append(item)
            except AttributeError:
                # Collection items with no name are ignored.
                pass
        exit(c)
