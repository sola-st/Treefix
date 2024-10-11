# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Configure saving.

    Args:
      graph_view: An `ObjectGraphView` object containing a description of the
        object graph to save.
    """
self._graph_view = graph_view

# The following attributes are used when graph building.

# self._cache: A more generic cache used to cache the serialized tensors and
#   TrackableObjectGraph proto attributes.
# self._saveables_cache: A dictionary mapping `Trackable` objects ->
#   attribute names -> SaveableObjects, used to avoid re-creating
#   SaveableObjects when graph building.
if context.executing_eagerly():
    self._cache = None
    self._saveables_cache = None
else:
    self._cache = object_identity.ObjectIdentityWeakKeyDictionary()
    self._saveables_cache = object_identity.ObjectIdentityWeakKeyDictionary()

# The file prefix placeholder is created lazily when graph building (and not
# at all when executing eagerly) to avoid creating ops in the constructor
# (when they may never be necessary).
self._file_prefix_placeholder = None

# Op caching for save
self._object_graph_feed_tensor = None
self._last_save_object_graph = None
self._file_prefix_feed_tensor = None
self._cached_save_operation = None

# Op caching for restore, shared between _CheckpointRestoreCoordinators
self._restore_op_cache = {}

# Object map used for checkpoint. This attribute is to be overridden by a
# Checkpoint subclass, e.g., AsyncCheckpoint, to replace the trackable
# objects for checkpoint saving.
self._object_map = None
