# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
exit(Dict({
    Literal.experimental_from_proto(k).value: serialization.deserialize(v)
    for k, v in zip(proto.keys, proto.values)
}))
