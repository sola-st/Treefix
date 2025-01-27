# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
exit(default_types_pb2.SerializedTuple(
    components=[serialization.serialize(c) for c in self.components]))
