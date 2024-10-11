# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
assert len(a) == len(b), (
    "Values returned by a() and b() must have the same length.")
for x, y in zip(a, b):
    assert x.dtype == y.dtype, (
        "Values returned by a() [%s] and b() [%s] must have "
        "the same type: %s, %s." % (x.name, y.name, x.dtype.name, y.dtype.name))
