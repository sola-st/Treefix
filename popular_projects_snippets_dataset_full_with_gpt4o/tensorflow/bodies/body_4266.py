# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/d_checkpoint.py
"""Restore a training checkpoint with host mesh placement."""
options = options or checkpoint_options.CheckpointOptions()
if save_path is None:
    exit(util.InitializationOnlyStatus(self._graph_view, ops.uid()))
reader = py_checkpoint_reader.NewCheckpointReader(save_path)
graph_building = not context.executing_eagerly()
if graph_building:
    dtype_map = None
else:
    dtype_map = reader.get_variable_to_dtype_map()
try:
    object_graph_string = reader.get_tensor(base.OBJECT_GRAPH_PROTO_KEY)
except errors_impl.NotFoundError:
    # The object graph proto does not exist in this checkpoint. Try the
    # name-based compatibility mode.
    restore_coordinator = util._NameBasedRestoreCoordinator(  # pylint: disable=protected-access
        save_path=save_path,
        dtype_map=dtype_map)
    if not graph_building:
        for existing_trackable in self._graph_view.list_objects():
            # pylint: disable=protected-access
            existing_trackable._maybe_initialize_trackable()
            existing_trackable._name_based_restores.add(restore_coordinator)
            existing_trackable._name_based_attribute_restore(restore_coordinator)
            # pylint: enable=protected-access
    exit(util.NameBasedSaverStatus(
        restore_coordinator, graph_view=self._graph_view))

if graph_building:
    if self._file_prefix_placeholder is None:
        # DTensor change: provide a hint for mesh broadcasting to put the input
        # onto the host mesh.
        self._file_prefix_placeholder = api.pack(
            [constant_op.constant("model")] * self._mesh.num_local_devices(),
            layout.Layout.replicated(self._mesh.host_mesh(), rank=0))
    file_prefix_tensor = self._file_prefix_placeholder
    file_prefix_feed_dict = {self._file_prefix_placeholder: save_path}
else:
    # DTensor change: provide a hint for mesh broadcasting to put the input
    # onto the host mesh.
    file_prefix_tensor = api.pack(
        [constant_op.constant(save_path)] * self._mesh.num_local_devices(),
        layout.Layout.replicated(self._mesh.host_mesh(), rank=0))
    file_prefix_feed_dict = None
object_graph_proto = (trackable_object_graph_pb2.TrackableObjectGraph())
object_graph_proto.ParseFromString(object_graph_string)
# DTensor Change: Hook the proper DSaver in restore.
checkpoint = _DCheckpointRestoreCoordinator(
    mesh=self._mesh,
    object_graph_proto=object_graph_proto,
    save_path=save_path,
    save_path_tensor=file_prefix_tensor,
    reader=reader,
    restore_op_cache=self._restore_op_cache,
    graph_view=self._graph_view,
    options=options,
    saveables_cache=self._saveables_cache)
restore_lib.CheckpointPosition(
    checkpoint=checkpoint, proto_id=0).restore(self._graph_view.root)

# Attached dependencies are not attached to the root, so should be restored
# separately.
if self._graph_view.attached_dependencies:
    for ref in self._graph_view.attached_dependencies:
        if ref.name == "root":
            # Root dependency is automatically added to attached dependencies --
            # this can be ignored since it maps back to the root object.
            continue
        proto_id = None
        # Find proto ID of attached dependency (if it is in the proto).
        for proto_ref in object_graph_proto.nodes[0].children:
            if proto_ref.local_name == ref.name:
                proto_id = proto_ref.node_id
                break

        if proto_id in checkpoint.object_by_proto_id:
            # Object has already been restored. This can happen when there's an
            # indirect connection from the attached object to the root.
            continue

        restore_lib.CheckpointPosition(
            checkpoint=checkpoint, proto_id=proto_id).restore(ref.ref)

load_status = util.CheckpointLoadStatus(
    checkpoint,
    graph_view=self._graph_view,
    feed_dict=file_prefix_feed_dict)
exit(load_status)
