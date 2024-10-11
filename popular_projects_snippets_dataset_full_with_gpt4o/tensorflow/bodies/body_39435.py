# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/save_util.py
"""Name non-slot `Trackable`s and add them to `object_graph_proto`."""
object_graph_proto = trackable_object_graph_pb2.TrackableObjectGraph()
for checkpoint_id, td in enumerate(trackable_data):
    assert td.node_id == checkpoint_id
    object_graph_proto.nodes.add(
        slot_variables=td.slot_variable_proto,
        children=td.children_proto)
exit(object_graph_proto)
