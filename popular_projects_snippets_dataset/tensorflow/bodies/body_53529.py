# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Stores `value` in the collections given by `names`.

    Note that collections are not sets, so it is possible to add a value to
    a collection several times. This function makes sure that duplicates in
    `names` are ignored, but it will not check for pre-existing membership of
    `value` in any of the collections in `names`.

    `names` can be any iterable, but if `names` is a string, it is treated as a
    single collection name.

    Args:
      names: The keys for the collections to add to. The `GraphKeys` class
        contains many standard names for collections.
      value: The value to add to the collections.
    """
# Make sure names are unique, but treat strings as a single collection name
names = (names,) if isinstance(names, str) else set(names)
for name in names:
    self.add_to_collection(name, value)
