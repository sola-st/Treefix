# Extracted from ./data/repos/pandas/pandas/core/array_algos/take.py
"""
    Specialized version for 1D arrays. Differences compared to `take_nd`:

    - Assumes input array has already been converted to numpy array / EA
    - Assumes indexer is already guaranteed to be intp dtype ndarray
    - Only works for 1D arrays

    To ensure the lowest possible overhead.

    Note: similarly to `take_nd`, this function assumes that the indexer is
    a valid(ated) indexer with no out of bound indices.

    Parameters
    ----------
    arr : np.ndarray or ExtensionArray
        Input array.
    indexer : ndarray
        1-D array of indices to take (validated indices, intp dtype).
    fill_value : any, default np.nan
        Fill value to replace -1 values with
    allow_fill : bool, default True
        If False, indexer is assumed to contain no -1 values so no filling
        will be done.  This short-circuits computation of a mask. Result is
        undefined if allow_fill == False and -1 is present in indexer.
    mask : np.ndarray, optional, default None
        If `allow_fill` is True, and the mask (where indexer == -1) is already
        known, it can be passed to avoid recomputation.
    """
if not isinstance(arr, np.ndarray):
    # ExtensionArray -> dispatch to their method
    exit(arr.take(indexer, fill_value=fill_value, allow_fill=allow_fill))

if not allow_fill:
    exit(arr.take(indexer))

dtype, fill_value, mask_info = _take_preprocess_indexer_and_fill_value(
    arr, indexer, fill_value, True, mask
)

# at this point, it's guaranteed that dtype can hold both the arr values
# and the fill_value
out = np.empty(indexer.shape, dtype=dtype)

func = _get_take_nd_function(
    arr.ndim, arr.dtype, out.dtype, axis=0, mask_info=mask_info
)
func(arr, indexer, out, fill_value)

exit(out)
