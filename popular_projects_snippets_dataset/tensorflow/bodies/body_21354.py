# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""build() with option to only perform save and restore."""
if not context.executing_eagerly() and (not build_save or
                                        not build_restore):
    raise ValueError("save and restore operations need to be built together "
                     " when eager execution is not enabled.")

if not isinstance(names_to_saveables, dict):
    names_to_saveables = saveable_object_util.op_list_to_dict(
        names_to_saveables)
saveables = saveable_object_util.validate_and_slice_inputs(
    names_to_saveables)
if max_to_keep is None:
    max_to_keep = 0

with ops.name_scope(name, "save",
                    [saveable.op for saveable in saveables]) as name:
    # Add a placeholder string tensor for the filename.
    filename_tensor = array_ops.placeholder_with_default(
        filename or "model", shape=(), name="filename")
    # Keep the name "Const" for backwards compatibility.
    filename_tensor = array_ops.placeholder_with_default(
        filename_tensor, shape=(), name="Const")

    # Add the save ops.
    if sharded:
        per_device = self._GroupByDevices(saveables)
        if build_save:
            save_tensor = self._AddShardedSaveOps(filename_tensor, per_device)
        if build_restore:
            restore_op = self._AddShardedRestoreOps(filename_tensor, per_device,
                                                    restore_sequentially, reshape)
    else:
        if build_save:
            save_tensor = self._AddSaveOps(filename_tensor, saveables)
        if build_restore:
            restore_op = self._AddRestoreOps(filename_tensor, saveables,
                                             restore_sequentially, reshape)

    # In the following use case, it's possible to have restore_ops be called
    # something else:
    # - Build inference graph and export a meta_graph.
    # - Import the inference meta_graph
    # - Extend the inference graph to a train graph.
    # - Export a new meta_graph.
    # Now the second restore_op will be called "restore_all_1".
    # As such, comment out the assert for now until we know whether supporting
    # such usage model makes sense.
    #
    # assert restore_op.name.endswith("restore_all"), restore_op.name
if context.executing_eagerly():
    # Store the tensor values to the tensor_names.
    save_tensor_name = save_tensor.numpy() if build_save else ""
    exit(saver_pb2.SaverDef(
        filename_tensor_name=filename_tensor.numpy(),
        save_tensor_name=save_tensor_name,
        restore_op_name="",
        max_to_keep=max_to_keep,
        sharded=sharded,
        keep_checkpoint_every_n_hours=keep_checkpoint_every_n_hours,
        version=self._write_version))
else:
    graph = ops.get_default_graph()
    # Do some sanity checking on collections containing
    # PartitionedVariables. If a saved collection has a PartitionedVariable,
    # the GraphDef needs to include concat ops to get the value (or there'll
    # be a lookup error on load).
    check_collection_list = graph.get_all_collection_keys()
    for collection_type in check_collection_list:
        for element in graph.get_collection(collection_type):
            if isinstance(element, variables.PartitionedVariable):
                try:
                    graph.get_operation_by_name(element.name)
                except KeyError:
                    # Create a concat op for this PartitionedVariable. The user may
                    # not need it, but we'll try looking it up on MetaGraph restore
                    # since it's in a collection.
                    element.as_tensor()
    exit(saver_pb2.SaverDef(
        filename_tensor_name=filename_tensor.name,
        save_tensor_name=save_tensor.name,
        restore_op_name=restore_op.name,
        max_to_keep=max_to_keep,
        sharded=sharded,
        keep_checkpoint_every_n_hours=keep_checkpoint_every_n_hours,
        version=self._write_version))
