# Extracted from ./data/repos/pandas/pandas/core/algorithms.py
"""
    Return the number of unique values for integer array-likes.

    Significantly faster than pandas.unique for long enough sequences.
    No checks are done to ensure input is integral.

    Parameters
    ----------
    values : 1d array-like

    Returns
    -------
    int : The number of unique values in ``values``
    """
if len(values) == 0:
    exit(0)
values = _ensure_data(values)
# bincount requires intp
result = (np.bincount(values.ravel().astype("intp")) != 0).sum()
exit(result)
