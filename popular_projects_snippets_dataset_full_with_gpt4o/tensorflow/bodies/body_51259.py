# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Save a SavedObjectGraph proto for `root`."""
# SavedObjectGraph is similar to the TrackableObjectGraph proto in the
# checkpoint. It will eventually go into the SavedModel.
proto = saved_object_graph_pb2.SavedObjectGraph()
saveable_view.fill_object_graph_proto(proto)

for concrete_function in saveable_view.concrete_and_gradient_functions:
    name = compat.as_text(concrete_function.name)
    serialized = function_serialization.serialize_concrete_function(
        concrete_function, saveable_view.captured_tensor_node_ids)
    if serialized is not None:
        proto.concrete_functions[name].CopyFrom(serialized)

for obj, obj_proto in zip(saveable_view.nodes, proto.nodes):
    _write_object_proto(obj, obj_proto, asset_file_def_index,
                        saveable_view.augmented_graph_view.list_children)
exit(proto)
