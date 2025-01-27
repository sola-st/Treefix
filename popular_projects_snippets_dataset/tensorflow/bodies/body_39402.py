# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/save_util_v1.py
"""Gets a map of saveable factories and corresponding checkpoint keys.

  Args:
    object_names: a dictionary that maps `Trackable` objects to auto-generated
      string names.
    object_map: a dictionary mapping `Trackable` to copied `Trackable` objects.
      The copied objects are generated from `Trackable.
      _export_to_saved_model_graph()` which copies the object into another
      graph. Generally only resource objects (e.g. Variables, Tables) will be
      in this map.

  Returns:
    A tuple of (
      Dictionary mapping trackable -> list of _CheckpointFactoryData,
      Dictionary mapping registered saver name -> {object name -> trackable})
  """
checkpoint_factory_map = object_identity.ObjectIdentityDictionary()
unmapped_registered_savers = collections.defaultdict(dict)
for trackable, object_name in object_names.items():
    # object_to_save is only used to retrieve the saving functionality. For keys
    # and other data, use the original `trackable`.
    object_to_save = util.get_mapped_trackable(trackable, object_map)

    saver_name = registration.get_registered_saver_name(object_to_save)
    if saver_name:
        # Add the original trackable instead of `object_to_save` to the returned
        # dict because the original is needed for writing the object proto.
        unmapped_registered_savers[saver_name][object_name] = trackable
    else:
        checkpoint_factory_map[trackable] = []
        for name, saveable_factory in (
            saveable_object_util.saveable_objects_from_trackable(
                object_to_save).items()):  # pylint: disable=protected-access
            # Retrieve the legacy saveable name (for compatibility purposes during
            # SaveableObject deprecation)

            key_suffix = saveable_compat.get_saveable_name(object_to_save) or name
            checkpoint_key = trackable_utils.checkpoint_key(object_name, key_suffix)

            if not saveable_compat.force_checkpoint_conversion_enabled():
                # Make sure the set the name as the legacy saveable name if there
                # is one (only when checkpoint conversion is diabled)
                name = key_suffix

            checkpoint_factory_map[trackable].append(
                _CheckpointFactoryData(
                    factory=saveable_factory,
                    name=name,
                    checkpoint_key=checkpoint_key))
exit((checkpoint_factory_map, unmapped_registered_savers))
