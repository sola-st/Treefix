# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/save_util.py
"""Gathers serialization objects, and creates a TrackableObjectGraph proto."""
# There are 3 types of checkpoint serialization types supported:
# 1. Trackables that override `Trackable._serialize_to_tensor()`.
# 2. PythonState: A special type of Trackable that serializes a Python string.
# 3. Registered Trackable Savers: For objects that need to define advanced
#    checkpointing operations not supported by (1) or (2).
trackable_data, node_ids = _gather_trackable_data(graph_view, object_map)
tensor_trackables, pystate_trackables, registered_trackables = (
    _split_trackables(trackable_data))

object_graph_proto = _fill_object_graph_proto(trackable_data)

serialized_tensors = _get_and_write_tensors_to_serialize(
    tensor_trackables,
    node_ids,
    call_with_mapped_captures,
    cache,
    object_graph_proto)
registered_savers = _get_and_write_registered_savers(
    registered_trackables, object_graph_proto)

# PythonState trackables must be treated differently depending on if the
# checkpoint is being saved in TF1 graph mode (`cache` exists) or
# eager mode (`cache` is None).
if cache is None:
    # When the tensor cache is None, get the serialized tensors directly.
    feed_additions = None
    serialized_tensors.update(_get_and_write_tensors_to_serialize(
        pystate_trackables,
        node_ids,
        call_with_mapped_captures,
        cache,
        object_graph_proto))
else:
    # Python state is not automatically updated within a TF session so these
    # values must be passed to sess.run(feed_additions=...).
    new_serialized_tensors, feed_additions = (
        _get_and_write_pystate_feed_additions(pystate_trackables,
                                              cache,
                                              object_graph_proto))
    serialized_tensors.update(new_serialized_tensors)

# Gather all trackables that have checkpoint values or descendants with
# checkpoint values, and add that info to the proto.
util.add_checkpoint_values_check(object_graph_proto)
exit((serialized_tensors, feed_additions, registered_savers,
        object_graph_proto))
