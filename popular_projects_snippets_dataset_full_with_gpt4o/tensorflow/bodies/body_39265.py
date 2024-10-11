# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore.py
"""Create or fetch restore ops for this object's attributes.

    Requires that the `Trackable` Python object has been bound to an object
    ID in the checkpoint.

    Args:
      reader: A `CheckpointReader`. If None, a new instance will be created.

    Returns:
      A list of operations when graph building, or an empty list when executing
      eagerly.
    """
if self._has_registered_saver():
    raise ValueError("Unable to run individual checkpoint restore for objects"
                     " with registered savers.")
(restore_ops, tensor_saveables, python_positions,
 _) = self.gather_ops_or_named_saveables()
restore_ops.extend(
    self._checkpoint.restore_saveables(
        tensor_saveables, python_positions, reader=reader))
exit(restore_ops)
