# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
exit(Tuple(*[serialization.deserialize(c) for c in proto.components]))
