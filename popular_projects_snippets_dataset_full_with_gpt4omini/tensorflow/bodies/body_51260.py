# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Saves an object into SavedObject proto."""
if isinstance(obj, asset.Asset):
    proto.asset.SetInParent()
    proto.asset.asset_file_def_index = asset_file_def_index[obj]
elif resource_variable_ops.is_resource_variable(obj):
    options = save_context.get_save_options()
    obj._write_object_proto(proto, options)  # pylint: disable=protected-access
elif isinstance(obj, def_function.Function):
    proto.function.CopyFrom(
        function_serialization.serialize_function(
            obj, [x.ref for x in list_children_fn(obj)]))
elif isinstance(obj, defun.ConcreteFunction):
    proto.bare_concrete_function.CopyFrom(
        function_serialization.serialize_bare_concrete_function(obj))
elif isinstance(obj, _CapturedTensor):
    proto.captured_tensor.name = obj.name
    proto.captured_tensor.concrete_function = obj.concrete_function
elif isinstance(obj, resource.CapturableResource):
    proto.resource.device = obj._resource_device  # pylint: disable=protected-access
else:
    registered_type_proto = revived_types.serialize(obj)
    if registered_type_proto is None:
        # Fallback for types with no matching registration
        # pylint:disable=protected-access
        registered_type_proto = saved_object_graph_pb2.SavedUserObject(
            identifier=obj._object_identifier,
            version=versions_pb2.VersionDef(
                producer=1, min_consumer=1, bad_consumers=[]))
        # pylint:enable=protected-access
    proto.user_object.CopyFrom(registered_type_proto)

registered_name = registration.get_registered_class_name(obj)
if registered_name:
    proto.registered_name = registered_name
    serialized_user_proto = obj._serialize_to_proto(object_proto=proto)  # pylint: disable=protected-access
    if serialized_user_proto is not None:
        proto.serialized_user_proto.Pack(serialized_user_proto)
