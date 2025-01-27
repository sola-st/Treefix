# Extracted from ./data/repos/pandas/pandas/io/common.py
"""
    Check whether or not the `columns` parameter
    could be converted into a MultiIndex.

    Parameters
    ----------
    columns : array-like
        Object which may or may not be convertible into a MultiIndex
    index_col : None, bool or list, optional
        Column or columns to use as the (possibly hierarchical) index

    Returns
    -------
    bool : Whether or not columns could become a MultiIndex
    """
if index_col is None or isinstance(index_col, bool):
    index_col = []

exit(bool(
    len(columns)
    and not isinstance(columns, MultiIndex)
    and all(isinstance(c, tuple) for c in columns if c not in list(index_col))
))
