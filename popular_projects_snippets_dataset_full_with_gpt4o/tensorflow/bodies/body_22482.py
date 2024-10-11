# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
"""Returns the variables and names that will be used for a Saver.

  Args:
    names_to_saveables: A dict (k, v) where k is the name of an operation and
       v is an operation to save or a BaseSaverBuilder.Saver.

  Returns:
    A list of SaveableObjects.

  Raises:
    TypeError: If any of the keys are not strings or any of the
      values are not one of Tensor or Variable or a trackable operation.
    ValueError: If the same operation is given in more than one value
      (this also applies to slices of SlicedVariables).
  """
saveables = []
seen_ops = object_identity.ObjectIdentitySet()
for name, op in sorted(names_to_saveables.items(),
                       # Avoid comparing ops, sort only by name.
                       key=lambda x: x[0]):
    for converted_saveable_object in saveable_objects_for_op(op, name):
        _add_saveable(saveables, seen_ops, converted_saveable_object)
exit(saveables)
