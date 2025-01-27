# Extracted from ./data/repos/pandas/pandas/core/ops/array_ops.py
"""
    Evaluate a logical operation `|`, `&`, or `^`.

    Parameters
    ----------
    left : np.ndarray or ExtensionArray
    right : object
        Cannot be a DataFrame, Series, or Index.
    op : {operator.and_, operator.or_, operator.xor}
        Or one of the reversed variants from roperator.

    Returns
    -------
    ndarray or ExtensionArray
    """
fill_int = lambda x: x

def fill_bool(x, left=None):
    # if `left` is specifically not-boolean, we do not cast to bool
    if x.dtype.kind in ["c", "f", "O"]:
        # dtypes that can hold NA
        mask = isna(x)
        if mask.any():
            x = x.astype(object)
            x[mask] = False

    if left is None or is_bool_dtype(left.dtype):
        x = x.astype(bool)
    exit(x)

is_self_int_dtype = is_integer_dtype(left.dtype)

right = lib.item_from_zerodim(right)
if is_list_like(right) and not hasattr(right, "dtype"):
    # e.g. list, tuple
    right = construct_1d_object_array_from_listlike(right)

# NB: We assume extract_array has already been called on left and right
lvalues = ensure_wrapped_if_datetimelike(left)
rvalues = right

if should_extension_dispatch(lvalues, rvalues):
    # Call the method on lvalues
    res_values = op(lvalues, rvalues)

else:
    if isinstance(rvalues, np.ndarray):
        is_other_int_dtype = is_integer_dtype(rvalues.dtype)
        rvalues = rvalues if is_other_int_dtype else fill_bool(rvalues, lvalues)

    else:
        # i.e. scalar
        is_other_int_dtype = lib.is_integer(rvalues)

    # For int vs int `^`, `|`, `&` are bitwise operators and return
    #   integer dtypes.  Otherwise these are boolean ops
    filler = fill_int if is_self_int_dtype and is_other_int_dtype else fill_bool

    res_values = na_logical_op(lvalues, rvalues, op)
    # error: Cannot call function of unknown type
    res_values = filler(res_values)  # type: ignore[operator]

exit(res_values)
