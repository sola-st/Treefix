# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/graph_view.py
"""Configure the graph view.

    Args:
      root: A `Trackable` object whose variables (including the variables of
        dependencies, recursively) should be saved. May be a weak reference.
      attached_dependencies: List of dependencies to attach to the root object.
        Used when saving a Checkpoint with a defined root object. To avoid
        reference cycles, this should use the WeakTrackableReference class.
    """
trackable_view.TrackableView.__init__(self, root)
# ObjectGraphView should never contain a strong reference to root, since it
# may result in a cycle:
#   root -> deferred dependencies -> CheckpointPosition
#   -> CheckpointRestoreCoordinator -> ObjectGraphView -> root
self._root_ref = (root if isinstance(root, weakref.ref)
                  else weakref.ref(root))
self._attached_dependencies = attached_dependencies
