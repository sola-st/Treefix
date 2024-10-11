# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/save_util_v1.py
"""Generates SaveableObjects and registered savers in the frozen graph."""
if to_graph:
    target_context = to_graph.as_default
else:
    target_context = ops.NullContextmanager
with target_context():
    named_saveable_objects, graph_proto, _, registered_savers = (
        serialize_gathered_objects(graph_view, object_map,
                                   call_with_mapped_captures, saveables_cache))
    with ops.device("/cpu:0"):
        object_graph_tensor = constant_op.constant(
            graph_proto.SerializeToString(), dtype=dtypes.string)
    named_saveable_objects.append(
        base.NoRestoreSaveable(
            tensor=object_graph_tensor, name=base.OBJECT_GRAPH_PROTO_KEY))
exit((named_saveable_objects, registered_savers))
