# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Restore a training checkpoint.

    Restores `root_trackable` and any objects that it tracks
    (transitive). Either assigns values immediately if variables to restore have
    been created already, or defers restoration until the variables are
    created. Dependencies added to the `root_trackable` passed to the
    constructor after this call will be matched if they have a corresponding
    object in the checkpoint.

    When building a graph, restorations are added to the graph but not run.

    ```python
    saver = Saver(root)
    saver.restore(path)
    ```

    To ensure that loading is complete and no more deferred restorations will
    take place, you can use the `assert_consumed()` method of the status object
    returned by the `restore` call.

    The assert will raise an exception unless every object was matched and all
    checkpointed values have a matching variable object.

    ```python
    saver = Saver(root)
    saver.restore(path).assert_consumed()
    ```

    When graph building, `assert_consumed()` indicates that all of the restore
    ops which will be created for this checkpoint have been created. They can be
    run via the `run_restore_ops()` function of the status object:

    ```python
    saver.restore(path).assert_consumed().run_restore_ops()
    ```

    If the checkpoint has not been consumed completely, then the list of restore
    ops will grow as more objects are added to the dependency graph.

    Name-based `tf.compat.v1.train.Saver` checkpoints can be loaded using this
    method. There is no deferred loading, and names are used to match
    variables. No restore ops are created/run until `run_restore_ops()` or
    `initialize_or_restore()` are called on the returned status object, even
    when executing eagerly. Re-encode name-based checkpoints using this
    object-based `Saver.save` as soon as possible.

    Args:
      save_path: The path to the checkpoint, as returned by `save` or
        `tf.train.latest_checkpoint`. If None (as when there is no latest
        checkpoint for `tf.train.latest_checkpoint` to return), returns an
        object which may run initializers for objects in the dependency graph.
        If the checkpoint was written by the name-based
        `tf.compat.v1.train.Saver`, names are used to match variables.
      options: Optional `tf.train.CheckpointOptions` object.

    Returns:
      A load status object, which can be used to make assertions about the
      status of checkpoint restoration and run initialization/restore ops
      (of type `CheckpointLoadStatus`, or `InitializationOnlyStatus` if
      `save_path` is `None`).

      If `save_path` points to a name-based checkpoint, a `NameBasedSaverStatus`
      object is returned which runs restore ops from a name-based saver.

    Raises:
      RuntimeError: When a checkpoint file saved by async checkpoint is not
        available upon restore().
    """
options = options or checkpoint_options.CheckpointOptions()
if save_path is None:
    exit(InitializationOnlyStatus(self._graph_view, ops.uid()))

# Wait until the ongoing checkpoint to finish.
# TODO(chienchunh): Allow to load the file while other checkpoint events
#                   are still ongiing. Need to add timeout mechanism along
#                   with conditional variables to notify when the checkpoint
#                   file is ready.
global _ASYNC_CHECKPOINT_THREAD
if _ASYNC_CHECKPOINT_THREAD is not None:
    _ASYNC_CHECKPOINT_THREAD.join()

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
    restore_coordinator = _NameBasedRestoreCoordinator(
        save_path=save_path,
        dtype_map=dtype_map)
    if not graph_building:
        for existing_trackable in util.list_objects(self._graph_view):
            # pylint: disable=protected-access
            existing_trackable._maybe_initialize_trackable()
            existing_trackable._name_based_restores.add(restore_coordinator)
            existing_trackable._name_based_attribute_restore(restore_coordinator)
            # pylint: enable=protected-access
    exit(NameBasedSaverStatus(
        restore_coordinator,
        object_graph_view=self._graph_view))

if graph_building:
    if self._file_prefix_placeholder is None:
        with ops.device("/cpu:0"):
            self._file_prefix_placeholder = constant_op.constant("model")
    file_prefix_tensor = self._file_prefix_placeholder
    file_prefix_feed_dict = {self._file_prefix_placeholder: save_path}
else:
    with ops.device("/cpu:0"):
        file_prefix_tensor = constant_op.constant(save_path)
    file_prefix_feed_dict = None
object_graph_proto = (trackable_object_graph_pb2.TrackableObjectGraph())
object_graph_proto.ParseFromString(object_graph_string)
checkpoint = _CheckpointRestoreCoordinator(
    object_graph_proto=object_graph_proto,
    save_path=save_path,
    save_path_tensor=file_prefix_tensor,
    reader=reader,
    restore_op_cache=self._restore_op_cache,
    graph_view=self._graph_view,
    options=options,
    saveables_cache=self._saveables_cache)
restore_lib.CheckpointPosition(
    checkpoint=checkpoint, proto_id=0).restore(self._graph_view.root,
                                               reader)

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

        if proto_id is None:
            # Could not find attached dependency in proto.
            continue

        restore_lib.CheckpointPosition(
            checkpoint=checkpoint,
            proto_id=proto_id).restore(ref.ref, reader)

load_status = CheckpointLoadStatus(
    checkpoint,
    graph_view=self._graph_view,
    feed_dict=file_prefix_feed_dict)
exit(load_status)
