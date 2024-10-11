# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
"""Traces all save and restore functions in the provided factory list.

  Args:
    obj: `Trackable` object.
    factory_data_list: List of `_CheckpointFactoryData`.

  Returns:
    Dict mapping atttribute names to tuples of concrete save/restore functions.
  """
saveable_fns = {}

for factory_data in factory_data_list:
    saveable_factory = factory_data.factory
    attribute_name = factory_data.name

    # If object revives as a resource (or TPU/Mirrored) variable,
    # there is no need to trace the save and restore functions.
    if (resource_variable_ops.is_resource_variable(obj) or
        resource_variable_ops.is_resource_variable(saveable_factory) or
        not callable(saveable_factory)):
        continue

    concrete_save, concrete_restore = (
        _trace_save_restore_functions(saveable_factory, obj))
    if not concrete_save:
        continue
    saveable_fns[attribute_name] = (concrete_save, concrete_restore)
exit(saveable_fns)
