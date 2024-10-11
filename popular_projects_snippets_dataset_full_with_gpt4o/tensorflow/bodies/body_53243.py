# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
"""Returns a TypeSpec instance based on the serialized proto.

    Do NOT override for custom non-TF types.

    Args:
      proto: Proto generated using 'experimental_as_proto'.
    """
exit(nested_structure_coder.decode_proto(
    struct_pb2.StructuredValue(type_spec_value=proto)))
