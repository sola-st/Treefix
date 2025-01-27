# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/d_checkpoint.py
super(DTensorCheckpoint, self).__init__(root=root, **kwargs)
self._mesh = mesh

saver_root = self
attached_dependencies = None
self._save_counter = None  # Created lazily for restore-on-create.
self._save_assign_op = None

if root:
    util._assert_trackable(root, "root")
    saver_root = root
    attached_dependencies = []

    # All keyword arguments (including root itself) are set as children
    # of root.
    kwargs["root"] = root
    root._maybe_initialize_trackable()

    self._save_counter = data_structures.NoDependency(
        root._lookup_dependency("save_counter"))
    self._root = data_structures.NoDependency(root)

for k, v in sorted(kwargs.items(), key=lambda item: item[0]):
    setattr(self, k, v)

    # Call getattr instead of directly using v because setattr converts
    # v to a Trackable data structure when v is a list/dict/tuple.
    converted_v = getattr(self, k)
    util._assert_trackable(converted_v, k)

    if root:
        # Make sure that root doesn't already have dependencies with these names
        attached_dependencies = attached_dependencies or []
        child = root._lookup_dependency(k)
        if child is None:
            attached_dependencies.append(base.TrackableReference(k, converted_v))
        elif child != converted_v:
            raise ValueError(
                "Cannot create a Checkpoint with keyword argument {name} if "
                "root.{name} already exists.".format(name=k))
    # DTensor Change:
    # Override the parents saver with DTrackableSaver with _SingleDeviceSaver.
self._saver = DTrackableSaver(
    mesh,
    graph_view_lib.ObjectGraphView(
        weakref.ref(saver_root),
        attached_dependencies=attached_dependencies))
