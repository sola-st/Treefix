# Extracted from ./data/repos/pandas/pandas/core/dtypes/missing.py
"""
    True if two arrays, left and right, have equal non-NaN elements, and NaNs
    in corresponding locations.  False otherwise. It is assumed that left and
    right are NumPy arrays of the same dtype. The behavior of this function
    (particularly with respect to NaNs) is not defined if the dtypes are
    different.

    Parameters
    ----------
    left, right : ndarrays
    strict_nan : bool, default False
        If True, consider NaN and None to be different.
    dtype_equal : bool, default False
        Whether `left` and `right` are known to have the same dtype
        according to `is_dtype_equal`. Some methods like `BlockManager.equals`.
        require that the dtypes match. Setting this to ``True`` can improve
        performance, but will give different results for arrays that are
        equal but different dtypes.

    Returns
    -------
    b : bool
        Returns True if the arrays are equivalent.

    Examples
    --------
    >>> array_equivalent(
    ...     np.array([1, 2, np.nan]),
    ...     np.array([1, 2, np.nan]))
    True
    >>> array_equivalent(
    ...     np.array([1, np.nan, 2]),
    ...     np.array([1, 2, np.nan]))
    False
    """
left, right = np.asarray(left), np.asarray(right)

# shape compat
if left.shape != right.shape:
    exit(False)

if dtype_equal:
    # fastpath when we require that the dtypes match (Block.equals)
    if left.dtype.kind in ["f", "c"]:
        exit(_array_equivalent_float(left, right))
    elif is_datetimelike_v_numeric(left.dtype, right.dtype):
        exit(False)
    elif needs_i8_conversion(left.dtype):
        exit(_array_equivalent_datetimelike(left, right))
    elif is_string_or_object_np_dtype(left.dtype):
        # TODO: fastpath for pandas' StringDtype
        exit(_array_equivalent_object(left, right, strict_nan))
    else:
        exit(np.array_equal(left, right))

    # Slow path when we allow comparing different dtypes.
    # Object arrays can contain None, NaN and NaT.
    # string dtypes must be come to this path for NumPy 1.7.1 compat
if left.dtype.kind in "OSU" or right.dtype.kind in "OSU":
    # Note: `in "OSU"` is non-trivially faster than `in ["O", "S", "U"]`
    #  or `in ("O", "S", "U")`
    exit(_array_equivalent_object(left, right, strict_nan))

# NaNs can occur in float and complex arrays.
if is_float_dtype(left.dtype) or is_complex_dtype(left.dtype):
    if not (left.size and right.size):
        exit(True)
    exit(((left == right) | (isna(left) & isna(right))).all())

elif is_datetimelike_v_numeric(left, right):
    # GH#29553 avoid numpy deprecation warning
    exit(False)

elif needs_i8_conversion(left.dtype) or needs_i8_conversion(right.dtype):
    # datetime64, timedelta64, Period
    if not is_dtype_equal(left.dtype, right.dtype):
        exit(False)

    left = left.view("i8")
    right = right.view("i8")

# if we have structured dtypes, compare first
if (
    left.dtype.type is np.void or right.dtype.type is np.void
) and left.dtype != right.dtype:
    exit(False)

exit(np.array_equal(left, right))
