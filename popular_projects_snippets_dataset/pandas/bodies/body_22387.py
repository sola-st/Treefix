# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
"""
    Extracts the union from lvals and rvals with respect to duplicates and nans in
    both arrays.

    Parameters
    ----------
    lvals: np.ndarray or ExtensionArray
        left values which is ordered in front.
    rvals: np.ndarray or ExtensionArray
        right values ordered after lvals.

    Returns
    -------
    np.ndarray or ExtensionArray
        Containing the unsorted union of both arrays.

    Notes
    -----
    Caller is responsible for ensuring lvals.dtype == rvals.dtype.
    """
from pandas import Series

l_count = value_counts(lvals, dropna=False)
r_count = value_counts(rvals, dropna=False)
l_count, r_count = l_count.align(r_count, fill_value=0)
final_count = np.maximum(l_count.values, r_count.values)
final_count = Series(final_count, index=l_count.index, dtype="int", copy=False)
if isinstance(lvals, ABCMultiIndex) and isinstance(rvals, ABCMultiIndex):
    unique_vals = lvals.append(rvals).unique()
else:
    if isinstance(lvals, ABCIndex):
        lvals = lvals._values
    if isinstance(rvals, ABCIndex):
        rvals = rvals._values
    unique_vals = unique(concat_compat([lvals, rvals]))
    unique_vals = ensure_wrapped_if_datetimelike(unique_vals)
repeats = final_count.reindex(unique_vals).values
exit(np.repeat(unique_vals, repeats))
