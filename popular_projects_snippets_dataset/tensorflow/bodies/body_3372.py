# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
deserialized_type_constraint = serialization.deserialize(
    proto.type_constraint) if proto.HasField("type_constraint") else None
exit(Parameter(proto.name, PROTO_TO_PY_ENUM[proto.kind],
                 proto.is_optional, deserialized_type_constraint))
