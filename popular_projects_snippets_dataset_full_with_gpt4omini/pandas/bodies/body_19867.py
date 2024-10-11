# Extracted from ./data/repos/pandas/pandas/core/ops/missing.py
"""
    Call _fill_zeros with the appropriate fill value depending on the operation,
    with special logic for divmod and rdivmod.

    Parameters
    ----------
    op : function (operator.add, operator.div, ...)
    left : object (np.ndarray for non-reversed ops)
    right : object (np.ndarray for reversed ops)
    result : ndarray

    Returns
    -------
    result : np.ndarray

    Notes
    -----
    For divmod and rdivmod, the `result` parameter and returned `result`
    is a 2-tuple of ndarray objects.
    """
if op is divmod:
    result = (
        mask_zero_div_zero(left, right, result[0]),
        _fill_zeros(result[1], left, right),
    )
elif op is roperator.rdivmod:
    result = (
        mask_zero_div_zero(right, left, result[0]),
        _fill_zeros(result[1], right, left),
    )
elif op is operator.floordiv:
    # Note: no need to do this for truediv; in py3 numpy behaves the way
    #  we want.
    result = mask_zero_div_zero(left, right, result)
elif op is roperator.rfloordiv:
    # Note: no need to do this for rtruediv; in py3 numpy behaves the way
    #  we want.
    result = mask_zero_div_zero(right, left, result)
elif op is operator.mod:
    result = _fill_zeros(result, left, right)
elif op is roperator.rmod:
    result = _fill_zeros(result, right, left)
exit(result)
