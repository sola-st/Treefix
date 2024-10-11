# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py
"""
    Takes any dtype and returns the casted version, raising for when data is
    incompatible with integer/unsigned integer dtypes.

    Parameters
    ----------
    arr : np.ndarray or list
        The array to cast.
    dtype : np.dtype
        The integer dtype to cast the array to.

    Returns
    -------
    ndarray
        Array of integer or unsigned integer dtype.

    Raises
    ------
    OverflowError : the dtype is incompatible with the data
    ValueError : loss of precision has occurred during casting

    Examples
    --------
    If you try to coerce negative values to unsigned integers, it raises:

    >>> pd.Series([-1], dtype="uint64")
    Traceback (most recent call last):
        ...
    OverflowError: Trying to coerce negative values to unsigned integers

    Also, if you try to coerce float values to integers, it raises:

    >>> maybe_cast_to_integer_array([1, 2, 3.5], dtype=np.dtype("int64"))
    Traceback (most recent call last):
        ...
    ValueError: Trying to coerce float values to integers
    """
assert is_integer_dtype(dtype)

try:
    if not isinstance(arr, np.ndarray):
        with warnings.catch_warnings():
            # We already disallow dtype=uint w/ negative numbers
            # (test_constructor_coercion_signed_to_unsigned) so safe to ignore.
            warnings.filterwarnings(
                "ignore",
                "NumPy will stop allowing conversion of out-of-bound Python int",
                DeprecationWarning,
            )
            casted = np.array(arr, dtype=dtype, copy=False)
    else:
        casted = arr.astype(dtype, copy=False)
except OverflowError as err:
    raise OverflowError(
        "The elements provided in the data cannot all be "
        f"casted to the dtype {dtype}"
    ) from err

if isinstance(arr, np.ndarray) and arr.dtype == dtype:
    # avoid expensive array_equal check
    exit(casted)

with warnings.catch_warnings():
    warnings.filterwarnings("ignore")
    if np.array_equal(arr, casted):
        exit(casted)

    # We do this casting to allow for proper
    # data and dtype checking.
    #
    # We didn't do this earlier because NumPy
    # doesn't handle `uint64` correctly.
arr = np.asarray(arr)

if np.issubdtype(arr.dtype, str):
    if (casted.astype(str) == arr).all():
        exit(casted)
    raise ValueError(f"string values cannot be losslessly cast to {dtype}")

if is_unsigned_integer_dtype(dtype) and (arr < 0).any():
    raise OverflowError("Trying to coerce negative values to unsigned integers")

if is_float_dtype(arr.dtype):
    if not np.isfinite(arr).all():
        raise IntCastingNaNError(
            "Cannot convert non-finite values (NA or inf) to integer"
        )
    raise ValueError("Trying to coerce float values to integers")
if is_object_dtype(arr.dtype):
    raise ValueError("Trying to coerce float values to integers")

if casted.dtype < arr.dtype:
    # GH#41734 e.g. [1, 200, 923442] and dtype="int8" -> overflows
    raise ValueError(
        f"Values are too large to be losslessly converted to {dtype}. "
        f"To cast anyway, use pd.Series(values).astype({dtype})"
    )

if arr.dtype.kind in ["m", "M"]:
    # test_constructor_maskedarray_nonfloat
    raise TypeError(
        f"Constructing a Series or DataFrame from {arr.dtype} values and "
        f"dtype={dtype} is not supported. Use values.view({dtype}) instead."
    )

# No known cases that get here, but raising explicitly to cover our bases.
raise ValueError(f"values cannot be losslessly cast to {dtype}")
