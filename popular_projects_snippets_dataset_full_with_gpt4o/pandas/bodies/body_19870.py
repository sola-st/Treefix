# Extracted from ./data/repos/pandas/pandas/core/ops/array_ops.py
"""
    Return the result of evaluating op on the passed in values.

    If native types are not compatible, try coercion to object dtype.

    Parameters
    ----------
    left : np.ndarray
    right : np.ndarray or scalar
        Excludes DataFrame, Series, Index, ExtensionArray.
    is_cmp : bool, default False
        If this a comparison operation.

    Returns
    -------
    array-like

    Raises
    ------
    TypeError : invalid operation
    """
if isinstance(right, str):
    # can never use numexpr
    func = op
else:
    func = partial(expressions.evaluate, op)

try:
    result = func(left, right)
except TypeError:
    if not is_cmp and (is_object_dtype(left.dtype) or is_object_dtype(right)):
        # For object dtype, fallback to a masked operation (only operating
        #  on the non-missing values)
        # Don't do this for comparisons, as that will handle complex numbers
        #  incorrectly, see GH#32047
        result = _masked_arith_op(left, right, op)
    else:
        raise

if is_cmp and (is_scalar(result) or result is NotImplemented):
    # numpy returned a scalar instead of operating element-wise
    # e.g. numeric array vs str
    # TODO: can remove this after dropping some future numpy version?
    exit(invalid_comparison(left, right, op))

exit(missing.dispatch_fill_zeros(op, left, right, result))
