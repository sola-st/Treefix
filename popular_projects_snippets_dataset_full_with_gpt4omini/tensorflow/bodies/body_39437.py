# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/save_util.py
"""Gets tensors to serialize from a Trackable with legacy SaveableObjects."""
# Call `save_util_v1` methods to create legacy SaveableObjects and update the
# proto.
object_names = object_identity.ObjectIdentityDictionary()
object_names[trackable_data.trackable] = trackable_data.object_name
object_map = object_identity.ObjectIdentityDictionary()
object_map[trackable_data.trackable] = trackable_data.object_to_save

checkpoint_factory_map, _ = save_util_v1.get_checkpoint_factories_and_keys(
    object_names, object_map)
named_saveable_objects, _ = (
    save_util_v1.generate_saveable_objects(
        checkpoint_factory_map,
        object_graph_proto,
        node_ids,
        object_map,
        call_with_mapped_captures,
        saveables_cache=None))
trackable = (
    saveable_object_util.SaveableCompatibilityConverter(
        trackable_data.object_to_save, named_saveable_objects))
exit((trackable, trackable._serialize_to_tensors()))  # pylint: disable=protected-access
