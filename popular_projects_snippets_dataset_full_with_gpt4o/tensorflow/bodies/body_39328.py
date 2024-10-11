# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/graph_view.py
"""Returns list of all child trackables attached to obj.

    Args:
      obj: A `Trackable` object.
      save_type: A string, can be 'savedmodel' or 'checkpoint'.
      **kwargs: kwargs to use when retrieving the object's children.

    Returns:
      List of all children attached to the object.
    """
children = []
for name, ref in super(ObjectGraphView,
                       self).children(obj, save_type, **kwargs).items():
    children.append(base.TrackableReference(name, ref))

# GraphView objects may define children of the root object that are not
# actually attached, e.g. a Checkpoint object's save_counter.
if obj is self.root and self._attached_dependencies:
    children.extend(self._attached_dependencies)
exit(children)
