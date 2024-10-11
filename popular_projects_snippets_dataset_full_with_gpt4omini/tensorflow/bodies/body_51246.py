# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Generates global and individual save/restore concrete functions.

  The global functions records the ops to save and restore the entire object to
  a file prefix, while the individual functions save and restore value tensors
  for resources.

  This function is intended to run on the output of
  `save_util_v1.get_checkpoint_factories_and_keys(object_names)`,
  which returns the generated a map of `_CheckpointFactoryData`.

  Args:
    checkpoint_factory_map: A dictionary mapping trackable objects to
      a list of `_CheckpointFactoryData`.

  Returns:
    Tuple of (
      saveable_fn_map: Maps obj -> factory name -> (concrete save, restore)
      )
  """
# Maps obj -> factory attribute_name -> (concrete save, concrete restore)
# This
saveable_fn_map = object_identity.ObjectIdentityDictionary()

for obj, factory_data_list in checkpoint_factory_map.items():
    if resource_variable_ops.is_resource_variable(obj) or not factory_data_list:
        # There is no need to trace the save and restore functions for variables.
        continue

    if factory_data_list[0].name == trackable_utils.SERIALIZE_TO_TENSORS_NAME:
        # Trace Trackable save and restore functions.
        assert len(factory_data_list) == 1
        saveable_fn_map[obj] = {trackable_utils.SERIALIZE_TO_TENSORS_NAME: (
            tracing_utils.trace_save_and_restore(obj))}
    else:
        # Trace deprecated SaveableObject save and restore functions.
        saveable_fn_map[obj] = (
            saveable_object_util.trace_save_restore_function_map(
                obj, factory_data_list))
exit(saveable_fn_map)
