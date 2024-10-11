# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops.py
"""Returns range(0, rank(x)) if axis is None."""
if axis is not None:
    exit(axis)
else:
    try:
        x_rank = x.shape.rank
    except AttributeError:
        x_rank = None

    # Fast path: avoid creating Rank and Range ops if ndims is known.
    if x_rank:
        exit(constant_op.constant(np.arange(x_rank, dtype=np.int32)))
    else:
        # Otherwise, we rely on Range and Rank to do the right thing at run-time.
        exit(range(0, array_ops.rank(x)))
