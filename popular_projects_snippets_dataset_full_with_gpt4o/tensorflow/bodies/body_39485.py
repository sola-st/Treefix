# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Run or build restore operations for SaveableObjects.

    Args:
      tensor_saveables: `SaveableObject`s which correspond to Tensors.
      python_positions: List of CheckpointPositions bound to `PythonState`
        objects which must be restored eagerly.
      registered_savers: a dict mapping saver names-> object name -> Trackable.
      reader: A `CheckpointReader`. If None, a new instance will be created.

    Returns:
      When graph building, a list of restore operations, either cached or newly
      created, to restore `tensor_saveables`.
    """
if reader is None:
    reader = py_checkpoint_reader.NewCheckpointReader(self.save_path_string)

restore_ops = []
# Eagerly run restorations for Python state.
for position in python_positions:
    key = position.object_proto.attributes[0].checkpoint_key
    position.trackable.deserialize(reader.get_tensor(key))

# If we have new SaveableObjects, extract and cache restore ops.
if tensor_saveables or registered_savers:
    flat_saveables = saveable_object_util.validate_and_slice_inputs(
        tensor_saveables)
    new_restore_ops = functional_saver.MultiDeviceSaver.from_saveables(
        flat_saveables,
        registered_savers).restore(self.save_path_tensor, self.options)
    if not context.executing_eagerly():
        for name, restore_op in sorted(new_restore_ops.items()):
            restore_ops.append(restore_op)
            assert name not in self.restore_ops_by_name
            self.restore_ops_by_name[name] = restore_op
exit(restore_ops)
