# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/serialization.py
"""Converts a proto SerializedTraceType to instance of Serializable."""
for proto_class in PROTO_CLASS_TO_PY_CLASS:
    if proto.representation.Is(proto_class.DESCRIPTOR):
        actual_proto = proto_class()
        proto.representation.Unpack(actual_proto)
        exit(PROTO_CLASS_TO_PY_CLASS[proto_class].experimental_from_proto(
            actual_proto))

raise ValueError(
    "Can not deserialize proto of url: ", proto.representation.type_url,
    " since no matching Python class could be found. For value ",
    proto.representation.value)
