# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
"""
    Perform array addition that checks for underflow and overflow.

    Performs the addition of an int64 array and an int64 integer (or array)
    but checks that they do not result in overflow first. For elements that
    are indicated to be NaN, whether or not there is overflow for that element
    is automatically ignored.

    Parameters
    ----------
    arr : np.ndarray[int64] addend.
    b : array or scalar addend.
    arr_mask : np.ndarray[bool] or None, default None
        array indicating which elements to exclude from checking
    b_mask : np.ndarray[bool] or None, default None
        array or scalar indicating which element(s) to exclude from checking

    Returns
    -------
    sum : An array for elements x + b for each element x in arr if b is
          a scalar or an array for elements x + y for each element pair
          (x, y) in (arr, b).

    Raises
    ------
    OverflowError if any x + y exceeds the maximum or minimum int64 value.
    """
# For performance reasons, we broadcast 'b' to the new array 'b2'
# so that it has the same size as 'arr'.
b2 = np.broadcast_to(b, arr.shape)
if b_mask is not None:
    # We do the same broadcasting for b_mask as well.
    b2_mask = np.broadcast_to(b_mask, arr.shape)
else:
    b2_mask = None

# For elements that are NaN, regardless of their value, we should
# ignore whether they overflow or not when doing the checked add.
if arr_mask is not None and b2_mask is not None:
    not_nan = np.logical_not(arr_mask | b2_mask)
elif arr_mask is not None:
    not_nan = np.logical_not(arr_mask)
elif b_mask is not None:
    # error: Argument 1 to "__call__" of "_UFunc_Nin1_Nout1" has
    # incompatible type "Optional[ndarray[Any, dtype[bool_]]]";
    # expected "Union[_SupportsArray[dtype[Any]], _NestedSequence
    # [_SupportsArray[dtype[Any]]], bool, int, float, complex, str
    # , bytes, _NestedSequence[Union[bool, int, float, complex, str
    # , bytes]]]"
    not_nan = np.logical_not(b2_mask)  # type: ignore[arg-type]
else:
    not_nan = np.empty(arr.shape, dtype=bool)
    not_nan.fill(True)

# gh-14324: For each element in 'arr' and its corresponding element
# in 'b2', we check the sign of the element in 'b2'. If it is positive,
# we then check whether its sum with the element in 'arr' exceeds
# np.iinfo(np.int64).max. If so, we have an overflow error. If it
# it is negative, we then check whether its sum with the element in
# 'arr' exceeds np.iinfo(np.int64).min. If so, we have an overflow
# error as well.
i8max = lib.i8max
i8min = iNaT

mask1 = b2 > 0
mask2 = b2 < 0

if not mask1.any():
    to_raise = ((i8min - b2 > arr) & not_nan).any()
elif not mask2.any():
    to_raise = ((i8max - b2 < arr) & not_nan).any()
else:
    to_raise = ((i8max - b2[mask1] < arr[mask1]) & not_nan[mask1]).any() or (
        (i8min - b2[mask2] > arr[mask2]) & not_nan[mask2]
    ).any()

if to_raise:
    raise OverflowError("Overflow in int64 addition")

result = arr + b
if arr_mask is not None or b2_mask is not None:
    np.putmask(result, ~not_nan, iNaT)

exit(result)
