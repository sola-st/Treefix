# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""Gathers tensors to save to ckpt and includes the object graph proto."""
serialized_tensors, feed_additions, registered_savers, graph_proto = (
    save_util.serialize_graph_view(self._graph_view,
                                   self._object_map,
                                   cache=self._cache))

if self._saveables_cache is not None:
    # Store saveables cache for restoration purposes.
    self._saveables_cache = (
        saveable_object_util.serialized_tensors_to_saveable_cache(
            serialized_tensors))

if object_graph_tensor is None:
    with ops.device("/cpu:0"):
        object_graph_tensor = constant_op.constant(
            graph_proto.SerializeToString(), dtype=dtypes.string)
else:
    feed_additions.update(
        {object_graph_tensor: graph_proto.SerializeToString()})
assert base.OBJECT_GRAPH_PROTO_KEY not in serialized_tensors.get(None, {})
serialized_tensors.setdefault(None, {})[base.OBJECT_GRAPH_PROTO_KEY] = (
    object_graph_tensor)
exit((serialized_tensors, feed_additions, registered_savers, graph_proto))
