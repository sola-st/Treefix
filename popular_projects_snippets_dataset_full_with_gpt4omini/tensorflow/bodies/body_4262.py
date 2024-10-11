# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/d_checkpoint.py
"""Run or build restore operations for SaveableObjects.

    Args:
      tensor_saveables: `SaveableObject`s which correspond to Tensors.
      python_positions: `CheckpointPosition`s which correspond to `PythonState`
        Trackables bound to the checkpoint.
      registered_savers: a dict mapping saver names-> object name -> Trackable.
        This argument is not implemented for DTensorCheckpoint.
      reader: A CheckpointReader. Creates one lazily if None.

    Returns:
      When graph building, a list of restore operations, either cached or newly
      created, to restore `tensor_saveables`.
    """
del registered_savers

restore_ops = []
# Eagerly run restorations for Python state.
if python_positions:
    # Lazily create the NewCheckpointReader, since this requires file access
    # and we may not have any Python saveables.
    if reader is None:
        reader = py_checkpoint_reader.NewCheckpointReader(self.save_path_string)
    for position in python_positions:
        key = position.object_proto.attributes[0].checkpoint_key
        position.trackable.deserialize(reader.get_tensor(key))

    # If we have new SaveableObjects, extract and cache restore ops.
if tensor_saveables:
    validated_saveables = saveable_object_util.validate_and_slice_inputs(
        tensor_saveables)
    validated_names = set(saveable.name for saveable in validated_saveables)
    if set(tensor_saveables.keys()) != validated_names:
        raise AssertionError(
            ("Saveable keys changed when validating. Got back %s, was "
             "expecting %s") % (tensor_saveables.keys(), validated_names))
    # DTensor change: Use _DSaver that does restore on DTensor with
    # customized DTensorRestoreV2 op.
    new_restore_ops = _DSaver(self._mesh, validated_saveables).restore(
        self.save_path_tensor, self.options)
    if not context.executing_eagerly():
        for name, restore_op in sorted(new_restore_ops.items()):
            restore_ops.append(restore_op)
            assert name not in self.restore_ops_by_name
            self.restore_ops_by_name[name] = restore_op
exit(restore_ops)
