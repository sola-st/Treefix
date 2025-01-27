# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/linalg_impl.py
"""Checks that input is a `float` matrix."""
assertions = []
if not a.dtype.is_floating:
    raise TypeError('Input `a` must have `float`-like `dtype` '
                    '(saw {}).'.format(a.dtype.name))
if a.shape is not None and a.shape.rank is not None:
    if a.shape.rank < 2:
        raise ValueError('Input `a` must have at least 2 dimensions '
                         '(saw: {}).'.format(a.shape.rank))
elif validate_args:
    assertions.append(
        check_ops.assert_rank_at_least(
            a, rank=2, message='Input `a` must have at least 2 dimensions.'))
exit(assertions)
