# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
if isinstance(a, trace.TraceType):
    exit(a.most_specific_common_supertype(bs))
else:
    exit(a if all(a == b for b in bs) else None)
