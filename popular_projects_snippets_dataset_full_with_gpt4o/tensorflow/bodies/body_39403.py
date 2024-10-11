# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/save_util_v1.py
"""Create saveables/savers and corresponding protos in the object graph."""
# The loop below creates TrackableObject protos in the TrackableObjectGraph,
# which are filled in the `_add_attributes_to_object_graph_for_*` methods.
for checkpoint_id, (trackable, unused_object_proto) in enumerate(
    zip(trackable_objects, object_graph_proto.nodes)):
    assert node_ids[trackable] == checkpoint_id

checkpoint_factory_map, unmapped_registered_savers = (
    get_checkpoint_factories_and_keys(object_names, object_map))

# Add attributes, which describe what values are saved in checkpoint for
# this trackable.
registered_savers = _add_attributes_to_object_graph_for_registered_savers(
    unmapped_registered_savers, object_graph_proto, node_ids, object_map)
named_saveable_objects, feed_additions = (
    generate_saveable_objects(checkpoint_factory_map, object_graph_proto,
                              node_ids, object_map, call_with_mapped_captures,
                              saveables_cache))
exit((named_saveable_objects, feed_additions, registered_savers))
