# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
exit(Attrs(
    proto.named_attributes.type_name,
    tuple(proto.named_attributes.attribute_names),
    Tuple.experimental_from_proto(
        proto.named_attributes.attributes).components))
