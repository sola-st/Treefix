# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/trackable_view.py
"""Configure the trackable view.

    Args:
      root: A `Trackable` object whose variables (including the variables of
        dependencies, recursively) should be saved. May be a weak reference.
    """
# TrackableView should never contain a strong reference to root, since it
# may result in a cycle:
#   root -> deferred dependencies -> CheckpointPosition
#   -> CheckpointRestoreCoordinator -> TrackableView -> root
self._root_ref = (root if isinstance(root, weakref.ref)
                  else weakref.ref(root))
