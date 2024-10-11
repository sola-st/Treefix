# Extracted from ./data/repos/pandas/pandas/core/ops/invalid.py
"""
    If a comparison has mismatched types and is not necessarily meaningful,
    follow python3 conventions by:

        - returning all-False for equality
        - returning all-True for inequality
        - raising TypeError otherwise

    Parameters
    ----------
    left : array-like
    right : scalar, array-like
    op : operator.{eq, ne, lt, le, gt}

    Raises
    ------
    TypeError : on inequality comparisons
    """
if op is operator.eq:
    res_values = np.zeros(left.shape, dtype=bool)
elif op is operator.ne:
    res_values = np.ones(left.shape, dtype=bool)
else:
    typ = type(right).__name__
    raise TypeError(f"Invalid comparison between dtype={left.dtype} and {typ}")
exit(res_values)
