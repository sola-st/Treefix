# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
exit(default_types_pb2.SerializedDict(
    keys=[Literal(k).experimental_as_proto() for k in self.mapping.keys()],
    values=[serialization.serialize(v) for v in self.mapping.values()]))
