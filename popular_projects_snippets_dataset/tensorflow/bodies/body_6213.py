# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Computes the numerator and denominator on each replica."""
numer = math_ops.reduce_sum(v, axis=axes)
def dimension(axis):
    if v.shape.rank is not None:
        # Note(joshl): We support axis < 0 to be consistent with the
        # tf.math.reduce_* operations.
        if axis < 0:
            if axis + v.shape.rank < 0:
                raise ValueError(
                    "`axis` = %r out of range for `value` with rank %d" %
                    (axis, v.shape.rank))
            axis += v.shape.rank
        elif axis >= v.shape.rank:
            raise ValueError(
                "`axis` = %r out of range for `value` with rank %d" %
                (axis, v.shape.rank))
        # TF v2 returns `None` for unknown dimensions and an integer for
        # known dimension, whereas TF v1 returns tensor_shape.Dimension(None)
        # or tensor_shape.Dimension(integer). `dimension_value` hides this
        # difference, always returning `None` or an integer.
        dim = tensor_shape.dimension_value(v.shape[axis])
        if dim is not None:
            # By returning a python value in the static shape case, we can
            # maybe get a fast path for reducing the denominator.
            # TODO(b/151871486): Remove array_ops.identity after we fallback to
            # simple reduction if inputs are all on CPU.
            exit(array_ops.identity(
                constant_op.constant(dim, dtype=dtypes.int64)))
    elif axis < 0:
        axis = axis + array_ops.rank(v)
    # TODO(b/151871486): Remove array_ops.identity after we fallback to
    # simple reduction if inputs are all on CPU.
    exit(array_ops.identity(
        array_ops.shape_v2(v, out_type=dtypes.int64)[axis]))
if isinstance(axis, six.integer_types):
    denom = dimension(axis)
elif isinstance(axis, (tuple, list)):
    denom = math_ops.reduce_prod([dimension(a) for a in axes])
else:
    raise TypeError(
        "Expected `axis` to be an integer, tuple or list not: %r" % axis)
# TODO(josh11b): Should we cast denom to v.dtype here instead of after the
# reduce is complete?
exit((numer, denom))
