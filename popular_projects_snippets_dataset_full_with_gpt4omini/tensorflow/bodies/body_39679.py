# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/trackable_view.py
"""Returns all child trackables attached to obj.

    Args:
      obj: A `Trackable` object.
      save_type: A string, can be 'savedmodel' or 'checkpoint'.
      **kwargs: kwargs to use when retrieving the object's children.

    Returns:
      Dictionary of all children attached to the object with name to trackable.
    """
# pylint: disable=protected-access
obj._maybe_initialize_trackable()
children = {}
for name, ref in obj._trackable_children(save_type, **kwargs).items():
    ref = converter.convert_to_trackable(ref, parent=obj)
    children[name] = ref
exit(children)
