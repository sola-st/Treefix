# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/save_util.py
"""Gets tensors to serialize from a Trackable."""
trackable = trackable_data.object_to_save
save_fn = trackable._serialize_to_tensors  # pylint: disable=protected-access

if (call_with_mapped_captures and
    isinstance(save_fn, core.ConcreteFunction)):
    ret_tensor_dict = call_with_mapped_captures(save_fn, [])
else:
    ret_tensor_dict = save_fn()

# Create checkpoint keys for each entry in the returned tensor dict, and
# write each entry to the object proto.
tensor_dict = {}
for tensor_name, maybe_tensor in ret_tensor_dict.items():
    local_name = trackable_utils.escape_local_name(tensor_name)
    checkpoint_key = trackable_utils.checkpoint_key(trackable_data.object_name,
                                                    local_name)
    tensor_dict[checkpoint_key] = maybe_tensor

    # TODO(b/261786493): Delete this when DCheckpoint is removed.
    if isinstance(maybe_tensor, saveable_object_lib.SaveSpec):
        maybe_tensor.name = checkpoint_key
        maybe_tensor.slice_spec = ""

    if object_graph_proto is not None:
        object_graph_proto.nodes[trackable_data.node_id].attributes.add(
            name=local_name,
            checkpoint_key=checkpoint_key,
            full_name=util.get_full_name(trackable))

exit(tensor_dict)
