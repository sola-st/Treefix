# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/d_checkpoint.py
# Since the base Checkpoint class does not return SaveableObjects, re-use
# the saveables cache or generate new Saveables.
(serialized_tensors, feed_additions, registered_savers,
 graph_proto) = self._gather_serialized_tensors(object_graph_tensor)

saveables_dict = self._saveables_cache
if saveables_dict is None:
    # Get and remove object graph tensor from `serialized_tensors`, because
    # the function `serialized_tensors_to_saveable_cache` isn't equipped
    # to handle it.
    object_graph_tensor = serialized_tensors.pop(
        None)[base.OBJECT_GRAPH_PROTO_KEY]
    saveables_dict = (
        saveable_object_util.serialized_tensors_to_saveable_cache(
            serialized_tensors))
named_saveable_objects = []
for saveable_by_name in saveables_dict.values():
    for saveables in saveable_by_name.values():
        named_saveable_objects.extend(saveables)
named_saveable_objects.append(
    base.NoRestoreSaveable(
        tensor=object_graph_tensor,
        name=base.OBJECT_GRAPH_PROTO_KEY))
exit((named_saveable_objects, graph_proto, feed_additions,
        registered_savers))
