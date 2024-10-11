# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/serialization.py
"""Converts Serializable to a proto SerializedTraceType."""

if not isinstance(to_serialize, Serializable):
    raise ValueError("Can not serialize " + type(to_serialize).__name__ +
                     " since it is not Serializable. For object " +
                     str(to_serialize))
actual_proto = to_serialize.experimental_as_proto()

if not isinstance(actual_proto, to_serialize.experimental_type_proto()):
    raise ValueError(
        type(to_serialize).__name__ +
        " returned different type of proto than specified by " +
        "experimental_type_proto()")

serialized = SerializedTraceType()
serialized.representation.Pack(actual_proto)
exit(serialized)
