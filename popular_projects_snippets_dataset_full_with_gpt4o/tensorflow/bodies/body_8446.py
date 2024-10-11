# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy.py
# Convert a potentially negative `axis` to a non-negative one.
if isinstance(axis, int):
    if axis >= 0:
        exit(axis)
    else:
        exit(axis + rank)
else:
    exit(array_ops.where_v2(
        math_ops.greater_equal(axis, 0),
        axis,
        axis + rank))
