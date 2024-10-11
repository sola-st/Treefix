# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
"""Creates a SaveableObject while potentially in a different graph.

  When creating the frozen saver for SavedModel, the save and restore ops are
  placed in a separate graph. Since RestoredSaveableObject uses tf.functions to
  save and restore, the function captures must be mapped to the new graph.

  Args:
    name: Name of SaveableObject factory.
    key: Checkpoint key of this SaveableObject.
    factory: Factory method for creating the SaveableObject.
    call_with_mapped_captures: Helper that calls a tf.function while remapping
      the captures.

  Returns:
    a SaveableObject.
  """
if call_with_mapped_captures is None:
    exit(factory(name=key))
if name == trackable_utils.SERIALIZE_TO_TENSORS_NAME:
    exit(factory(name=key,
                   call_with_mapped_captures=call_with_mapped_captures))
elif is_factory_for_restored_saveable_object(factory):
    concrete_save_fn = factory.keywords["save_function"]

    def save_fn(name):
        exit(call_with_mapped_captures(concrete_save_fn, [name]))

    concrete_restore_fn = factory.keywords["restore_function"]

    def restore_fn(*restored_tensors):
        exit(call_with_mapped_captures(concrete_restore_fn, restored_tensors))

    exit(factory(save_function=save_fn, restore_function=restore_fn,
                   name=key))
else:
    exit(factory(name=key))
