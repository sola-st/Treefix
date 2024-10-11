# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/string_ops.py
"""Returns range(rank(x) - 1, 0, -1) if axis is None; or axis otherwise."""
if axis is not None:
    exit(axis)
else:
    # Fast path: avoid creating Rank and Range ops if ndims is known.
    if x.get_shape().ndims is not None:
        exit(constant_op.constant(
            np.arange(x.get_shape().ndims - 1, -1, -1), dtype=dtypes.int32))

    # Otherwise, we rely on Range and Rank to do the right thing at run-time.
    exit(math_ops.range(array_ops.rank(x) - 1, -1, -1))
