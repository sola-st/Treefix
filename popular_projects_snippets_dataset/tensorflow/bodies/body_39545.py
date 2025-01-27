# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Creates a training checkpoint for a single or group of objects.

    Args:
      root: The root object to checkpoint. `root` may be a trackable object or
        `WeakRef` of a trackable object.
      **kwargs: Keyword arguments are set as attributes of this object, and are
        saved with the checkpoint. All `kwargs` must be trackable objects, or a
        nested structure of trackable objects (`list`, `dict`, or `tuple`).

    Raises:
      ValueError: If `root` or the objects in `kwargs` are not trackable. A
        `ValueError` is also raised if the `root` object tracks different
        objects from the ones listed in attributes in kwargs (e.g.
        `root.child = A` and `tf.train.Checkpoint(root, child=B)` are
        incompatible).

    """
super().__init__()
global _END_TIME_OF_LAST_WRITE
with _END_TIME_OF_LAST_WRITE_LOCK:
    if _END_TIME_OF_LAST_WRITE is None:
        _END_TIME_OF_LAST_WRITE = time.time()

    # Store a reference to root and kwargs if we need to instantiate an
    # AsyncCheckpointer later.
self._root = root
self._kwargs = kwargs
self._delete_tracking("_kwargs")

# Don't instantiate the AsyncCheckpointer unless required.
self._async_checkpointer_impl = None

# Store checkpoint options during the save/write calls so that subsequent
# read/restore calls are done properly. This is only populated when
# async read/write is enabled.
self._checkpoint_options = None

attached_dependencies = None
self._save_counter = None  # Created lazily for restore-on-create.
self._save_assign_op = None

if root:
    trackable_root = root() if isinstance(root, weakref.ref) else root
    _assert_trackable(trackable_root, "root")
    attached_dependencies = []

    # All keyword arguments (including root itself) are set as children
    # of root.
    kwargs["root"] = root
    trackable_root._maybe_initialize_trackable()

    self._save_counter = data_structures.NoDependency(
        trackable_root._lookup_dependency("save_counter"))

for k, v in sorted(kwargs.items(), key=lambda item: item[0]):
    setattr(self, k, v)

    # Call getattr instead of directly using v because setattr converts
    # v to a Trackable data structure when v is a list/dict/tuple.
    converted_v = getattr(self, k)
    if isinstance(converted_v, weakref.ref):
        converted_v = converted_v()
    _assert_trackable(converted_v, k)

    if root:
        # Make sure that root doesn't already have dependencies with these names
        child = trackable_root._lookup_dependency(k)
        if child is None:
            attached_dependencies.append(
                base.WeakTrackableReference(k, converted_v))
        elif child != converted_v:
            raise ValueError(
                f"Cannot create a Checkpoint with keyword argument {k} if "
                f"root.{k} already exists.")

self._saver = TrackableSaver(
    graph_view_lib.ObjectGraphView(
        root if root else self,
        attached_dependencies=attached_dependencies))
self._attached_dependencies = data_structures.NoDependency(
    attached_dependencies)
