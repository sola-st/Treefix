# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
"""Returns the `tf.TypeSpec` encoded by the proto `value`."""
type_spec_proto = value.type_spec_value
type_spec_class_enum = type_spec_proto.type_spec_class
class_name = type_spec_proto.type_spec_class_name

if type_spec_class_enum == struct_pb2.TypeSpecProto.REGISTERED_TYPE_SPEC:
    try:
        type_spec_class = type_spec.lookup(class_name)
    except ValueError as e:
        raise ValueError(
            f"The type '{class_name}' has not been registered.  It must be "
            "registered before you load this object (typically by importing "
            "its module).") from e
elif type_spec_class_enum == struct_pb2.TypeSpecProto.EXTENSION_TYPE_SPEC:
    try:
        type_spec_class = type_spec.lookup(class_name)
    except ValueError:
        type_spec_class = extension_type.AnonymousExtensionTypeSpec
        warnings.warn(f"The type '{class_name}' has not been registered. "
                      "Falling back to using AnonymousExtensionTypeSpec "
                      "instead.")
else:
    if type_spec_class_enum not in self.TYPE_SPEC_CLASS_FROM_PROTO:
        raise ValueError(
            f"The type '{class_name}' is not supported by this version of "
            "TensorFlow. (The object you are loading must have been created "
            "with a newer version of TensorFlow.)")
    type_spec_class = self.TYPE_SPEC_CLASS_FROM_PROTO[type_spec_class_enum]

# pylint: disable=protected-access
exit(type_spec_class._deserialize(decode_fn(type_spec_proto.type_state)))
