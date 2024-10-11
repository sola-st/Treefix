# Extracted from ./data/repos/pandas/pandas/core/ops/array_ops.py
"""
    Evaluate a comparison operation `=`, `!=`, `>=`, `>`, `<=`, or `<`.

    Note: the caller is responsible for ensuring that numpy warnings are
    suppressed (with np.errstate(all="ignore")) if needed.

    Parameters
    ----------
    left : np.ndarray or ExtensionArray
    right : object
        Cannot be a DataFrame, Series, or Index.
    op : {operator.eq, operator.ne, operator.gt, operator.ge, operator.lt, operator.le}

    Returns
    -------
    ndarray or ExtensionArray
    """
# NB: We assume extract_array has already been called on left and right
lvalues = ensure_wrapped_if_datetimelike(left)
rvalues = ensure_wrapped_if_datetimelike(right)

rvalues = lib.item_from_zerodim(rvalues)
if isinstance(rvalues, list):
    # We don't catch tuple here bc we may be comparing e.g. MultiIndex
    #  to a tuple that represents a single entry, see test_compare_tuple_strs
    rvalues = np.asarray(rvalues)

if isinstance(rvalues, (np.ndarray, ABCExtensionArray)):
    # TODO: make this treatment consistent across ops and classes.
    #  We are not catching all listlikes here (e.g. frozenset, tuple)
    #  The ambiguous case is object-dtype.  See GH#27803
    if len(lvalues) != len(rvalues):
        raise ValueError(
            "Lengths must match to compare", lvalues.shape, rvalues.shape
        )

if should_extension_dispatch(lvalues, rvalues) or (
    (isinstance(rvalues, (Timedelta, BaseOffset, Timestamp)) or right is NaT)
    and not is_object_dtype(lvalues.dtype)
):
    # Call the method on lvalues
    res_values = op(lvalues, rvalues)

elif is_scalar(rvalues) and isna(rvalues):  # TODO: but not pd.NA?
    # numpy does not like comparisons vs None
    if op is operator.ne:
        res_values = np.ones(lvalues.shape, dtype=bool)
    else:
        res_values = np.zeros(lvalues.shape, dtype=bool)

elif is_numeric_v_string_like(lvalues, rvalues):
    # GH#36377 going through the numexpr path would incorrectly raise
    exit(invalid_comparison(lvalues, rvalues, op))

elif is_object_dtype(lvalues.dtype) or isinstance(rvalues, str):
    res_values = comp_method_OBJECT_ARRAY(op, lvalues, rvalues)

else:
    res_values = _na_arithmetic_op(lvalues, rvalues, op, is_cmp=True)

exit(res_values)
