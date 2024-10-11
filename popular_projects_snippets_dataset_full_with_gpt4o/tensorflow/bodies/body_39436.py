# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/save_util.py
"""Creates dictionary of tensors to checkpoint, and updates the proto."""
# Maps trackable to the a dictionary of tensors, which maps
# checkpoint key (-> slice_spec) -> tensor.
serialized_tensors = object_identity.ObjectIdentityDictionary()

for td in tensor_trackables:
    if cache is not None and td.object_to_save in cache:
        trackable, tensor_dict, object_proto = cache[td.object_to_save]
        serialized_tensors[trackable] = tensor_dict
        object_graph_proto.nodes[td.node_id].attributes.MergeFrom(object_proto)
        continue

    legacy_name = saveable_compat.get_saveable_name(td.object_to_save) or ""

    if (not saveable_object_util.trackable_has_serialize_to_tensor(
        td.object_to_save) or
        legacy_name):
        # Use the legacy code path for objects that are using SaveableObjects
        # or the compat saveable name decorator.
        trackable, tensor_dict = _get_tensors_from_legacy_saveable(
            td, node_ids, call_with_mapped_captures, object_graph_proto)
    else:
        tensor_dict = _get_tensors_from_trackable(
            td, call_with_mapped_captures, object_graph_proto)
        trackable = td.object_to_save
    serialized_tensors[trackable] = tensor_dict

    if cache is not None and td.object_to_save not in cache:
        cache[td.object_to_save] = (
            trackable, tensor_dict,
            object_graph_proto.nodes[td.node_id].attributes)

exit(serialized_tensors)
