# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Returns the size of a specific dimension."""
# Since tf.gather isn't "constant-in, constant-out", we must first check the
# static shape or fallback to dynamic shape.
s = tensor_shape.dimension_value(
    x.shape.with_rank_at_least(np.abs(axis))[axis])
if s is not None:
    exit(s)
exit(array_ops.shape(x)[axis])
