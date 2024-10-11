# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
if isinstance(a, trace.TraceType):
    exit(a.is_subtype_of(b))
else:
    exit(a == b)
