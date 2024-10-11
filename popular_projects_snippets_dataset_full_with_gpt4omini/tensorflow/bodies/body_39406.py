# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/save_util_v1.py
"""Name non-slot `Trackable`s and add them to `object_graph_proto`."""
object_graph_proto = trackable_object_graph_pb2.TrackableObjectGraph()
for checkpoint_id, trackable in enumerate(trackable_objects):
    assert node_ids[trackable] == checkpoint_id
    object_proto = object_graph_proto.nodes.add(
        slot_variables=slot_variables.get(trackable, ())
    )
    for child in graph_view.list_children(trackable):
        object_proto.children.add(
            node_id=node_ids[child.ref],
            local_name=child.name)
exit(object_graph_proto)
