# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
"""
    Find indices where elements should be inserted to maintain order.

    Find the indices into a sorted array `arr` (a) such that, if the
    corresponding elements in `value` were inserted before the indices,
    the order of `arr` would be preserved.

    Assuming that `arr` is sorted:

    ======  ================================
    `side`  returned index `i` satisfies
    ======  ================================
    left    ``arr[i-1] < value <= self[i]``
    right   ``arr[i-1] <= value < self[i]``
    ======  ================================

    Parameters
    ----------
    arr: np.ndarray, ExtensionArray, Series
        Input array. If `sorter` is None, then it must be sorted in
        ascending order, otherwise `sorter` must be an array of indices
        that sort it.
    value : array-like or scalar
        Values to insert into `arr`.
    side : {'left', 'right'}, optional
        If 'left', the index of the first suitable location found is given.
        If 'right', return the last such index.  If there is no suitable
        index, return either 0 or N (where N is the length of `self`).
    sorter : 1-D array-like, optional
        Optional array of integer indices that sort array a into ascending
        order. They are typically the result of argsort.

    Returns
    -------
    array of ints or int
        If value is array-like, array of insertion points.
        If value is scalar, a single integer.

    See Also
    --------
    numpy.searchsorted : Similar method from NumPy.
    """
if sorter is not None:
    sorter = ensure_platform_int(sorter)

if (
    isinstance(arr, np.ndarray)
    and is_integer_dtype(arr.dtype)
    and (is_integer(value) or is_integer_dtype(value))
):
    # if `arr` and `value` have different dtypes, `arr` would be
    # recast by numpy, causing a slow search.
    # Before searching below, we therefore try to give `value` the
    # same dtype as `arr`, while guarding against integer overflows.
    iinfo = np.iinfo(arr.dtype.type)
    value_arr = np.array([value]) if is_scalar(value) else np.array(value)
    if (value_arr >= iinfo.min).all() and (value_arr <= iinfo.max).all():
        # value within bounds, so no overflow, so can convert value dtype
        # to dtype of arr
        dtype = arr.dtype
    else:
        dtype = value_arr.dtype

    if is_scalar(value):
        # We know that value is int
        value = cast(int, dtype.type(value))
    else:
        value = pd_array(cast(ArrayLike, value), dtype=dtype)
else:
    # E.g. if `arr` is an array with dtype='datetime64[ns]'
    # and `value` is a pd.Timestamp, we may need to convert value
    arr = ensure_wrapped_if_datetimelike(arr)

# Argument 1 to "searchsorted" of "ndarray" has incompatible type
# "Union[NumpyValueArrayLike, ExtensionArray]"; expected "NumpyValueArrayLike"
exit(arr.searchsorted(value, side=side, sorter=sorter))  # type: ignore[arg-type]
