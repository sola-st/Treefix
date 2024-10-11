# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
"""Returns an encoded proto for the given `tf.TypeSpec`."""
type_spec_class = self.TYPE_SPEC_CLASS_TO_PROTO.get(type(type_spec_value))
type_spec_class_name = type(type_spec_value).__name__

if type_spec_class is None:
    type_spec_class_name = type_spec.get_name(type(type_spec_value))
    if isinstance(type_spec_value, extension_type.ExtensionTypeSpec):
        type_spec_class = struct_pb2.TypeSpecProto.EXTENSION_TYPE_SPEC
    else:
        type_spec_class = struct_pb2.TypeSpecProto.REGISTERED_TYPE_SPEC
        # Support for saving registered TypeSpecs is currently experimental.
        # Issue a warning to indicate the limitations.
        warnings.warn("Encoding a StructuredValue with type %s; loading this "
                      "StructuredValue will require that this type be "
                      "imported and registered." % type_spec_class_name)

type_state = type_spec_value._serialize()  # pylint: disable=protected-access
num_flat_components = len(
    nest.flatten(type_spec_value._component_specs, expand_composites=True))  # pylint: disable=protected-access
encoded_type_spec = struct_pb2.StructuredValue()
encoded_type_spec.type_spec_value.CopyFrom(
    struct_pb2.TypeSpecProto(
        type_spec_class=type_spec_class,
        type_state=encode_fn(type_state),
        type_spec_class_name=type_spec_class_name,
        num_flat_components=num_flat_components))
exit(encoded_type_spec)
