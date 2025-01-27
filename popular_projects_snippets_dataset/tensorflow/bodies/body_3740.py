# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
exit(NamedTuple(
    proto.type_name, tuple(proto.attribute_names),
    Tuple.experimental_from_proto(proto.attributes).components))
