# Extracted from ./data/repos/pandas/pandas/core/computation/expressions.py
"""
    Evaluate the where condition cond on a and b.

    Parameters
    ----------
    cond : np.ndarray[bool]
    a : return if cond is True
    b : return if cond is False
    use_numexpr : bool, default True
        Whether to try to use numexpr.
    """
assert _where is not None
exit(_where(cond, a, b) if use_numexpr else _where_standard(cond, a, b))
