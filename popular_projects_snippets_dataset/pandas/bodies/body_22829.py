# Extracted from ./data/repos/pandas/pandas/core/array_algos/take.py

"""
    Specialized Cython take which sets NaN values in one pass

    This dispatches to ``take`` defined on ExtensionArrays. It does not
    currently dispatch to ``SparseArray.take`` for sparse ``arr``.

    Note: this function assumes that the indexer is a valid(ated) indexer with
    no out of bound indices.

    Parameters
    ----------
    arr : np.ndarray or ExtensionArray
        Input array.
    indexer : ndarray
        1-D array of indices to take, subarrays corresponding to -1 value
        indices are filed with fill_value
    axis : int, default 0
        Axis to take from
    fill_value : any, default np.nan
        Fill value to replace -1 values with
    allow_fill : bool, default True
        If False, indexer is assumed to contain no -1 values so no filling
        will be done.  This short-circuits computation of a mask.  Result is
        undefined if allow_fill == False and -1 is present in indexer.

    Returns
    -------
    subarray : np.ndarray or ExtensionArray
        May be the same type as the input, or cast to an ndarray.
    """
if fill_value is lib.no_default:
    fill_value = na_value_for_dtype(arr.dtype, compat=False)
elif isinstance(arr.dtype, np.dtype) and arr.dtype.kind in "mM":
    dtype, fill_value = maybe_promote(arr.dtype, fill_value)
    if arr.dtype != dtype:
        # EA.take is strict about returning a new object of the same type
        # so for that case cast upfront
        arr = arr.astype(dtype)

if not isinstance(arr, np.ndarray):
    # i.e. ExtensionArray,
    # includes for EA to catch DatetimeArray, TimedeltaArray
    if not is_1d_only_ea_obj(arr):
        # i.e. DatetimeArray, TimedeltaArray
        arr = cast("NDArrayBackedExtensionArray", arr)
        exit(arr.take(
            indexer, fill_value=fill_value, allow_fill=allow_fill, axis=axis
        ))

    exit(arr.take(indexer, fill_value=fill_value, allow_fill=allow_fill))

arr = np.asarray(arr)
exit(_take_nd_ndarray(arr, indexer, axis, fill_value, allow_fill))
