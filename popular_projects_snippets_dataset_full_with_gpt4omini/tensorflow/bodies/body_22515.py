# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
"""Converts a tensor dict to a SaveableObject cache.

  Args:
    serialized_tensors: Map from Trackable to a tensor dict. The tensor dict
      maps checkpoint key (-> slice_spec) -> Tensor

  Returns:
    A dict mapping Trackable objects to a map from local savable name to
    SaveableObject.
  """
saveables_cache = object_identity.ObjectIdentityWeakKeyDictionary()

for obj, tensor_dict in serialized_tensors.items():
    if not tensor_dict: continue
    if isinstance(obj, SaveableCompatibilityConverter):
        trackable_obj = obj.obj
        saveables_cache[trackable_obj] = {}
        for saveable in obj.saveables:
            local_name = trackable_utils.extract_local_name(saveable.name)
            saveables_cache[trackable_obj][local_name] = [saveable]
        continue

    specs = []
    # The local names and prefixes are computed to ensure that the generated
    # SaveableObject can call `Trackable._restore_from_tensors()`
    local_names = []
    prefix = saveable_compat.get_saveable_name(obj) or ""
    for checkpoint_key, maybe_tensor in tensor_dict.items():
        # Make sure that `maybe_tensor` is a dict from `slice_spec` to `tensor`.
        if not isinstance(maybe_tensor, dict):
            maybe_tensor = {"": maybe_tensor}

        for slice_spec, tensor in maybe_tensor.items():
            if isinstance(tensor, saveable_object.SaveSpec):
                specs.append(tensor)
            else:
                specs.append(saveable_object.SaveSpec(tensor,
                                                      slice_spec,
                                                      checkpoint_key))
        local_names.append(trackable_utils.extract_local_name(checkpoint_key,
                                                              prefix))

    object_name = trackable_utils.extract_object_name(
        next(iter(tensor_dict.keys())))
    saveables_cache[obj] = {
        trackable_utils.SERIALIZE_TO_TENSORS_NAME: [TrackableSaveable(
            obj, specs, object_name, local_names=local_names, prefix=prefix)]}
exit(saveables_cache)
