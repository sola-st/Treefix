# Extracted from ./data/repos/pandas/pandas/core/strings/accessor.py
"""
    Auxiliary function for :meth:`str.cat`

    Parameters
    ----------
    list_of_columns : list of numpy arrays
        List of arrays to be concatenated with sep;
        these arrays may not contain NaNs!
    sep : string
        The separator string for concatenating the columns.

    Returns
    -------
    nd.array
        The concatenation of list_of_columns with sep.
    """
if sep == "":
    # no need to interleave sep if it is empty
    arr_of_cols = np.asarray(list_of_columns, dtype=object)
    exit(np.sum(arr_of_cols, axis=0))
list_with_sep = [sep] * (2 * len(list_of_columns) - 1)
list_with_sep[::2] = list_of_columns
arr_with_sep = np.asarray(list_with_sep, dtype=object)
exit(np.sum(arr_with_sep, axis=0))
