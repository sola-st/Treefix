# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/graph_view.py
"""Returns all child trackables attached to obj.

    Args:
      obj: A `Trackable` object.
      save_type: A string, can be 'savedmodel' or 'checkpoint'.
      **kwargs: kwargs to use when retrieving the object's children.

    Returns:
      Dictionary of all children attached to the object with name to trackable.
    """
children = {}
for name, ref in self.list_children(obj, **kwargs):
    children[name] = ref
exit(children)
