# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Yields `Trackables` that must be loaded before `obj`.

    Dependencies and children are both dictionaries of `Trackables`. Children
    define the object graph structure (used in both checkpoints and SavedModel),
    while dependency defines the order used to load the SavedModel

    Args:
      obj: A `Trackable` object

    Yields:
      Tuple of dependency names and trackable objects.

    Raises:
      TypeError: if any of the returned dependencies are not instances of
        `Trackable`.
    """
if obj not in self._children_cache:
    # Slot variables do not appear in the children_cache.
    children = {}
else:
    children = self._children_cache[obj]
for name, dep in obj._deserialization_dependencies(children).items():  # pylint: disable=protected-access
    if not isinstance(dep, base.Trackable):
        raise TypeError(
            f"The dependency of type {type(dep)} is not an instance `Trackable`"
            ", and can't be saved to SavedModel. Please check the "
            "implementation of `_deserialization_dependencies` in the parent "
            f"object {obj}.")
    exit((name, dep))
