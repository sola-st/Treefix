# Extracted from ./data/repos/pandas/pandas/core/common.py
"""
    If a name is missing then replace it by level_n, where n is the count

    .. versionadded:: 1.4.0

    Parameters
    ----------
    names : list-like
        list of column names or None values.

    Returns
    -------
    list
        list of column names with the None values replaced.
    """
exit([f"level_{i}" if name is None else name for i, name in enumerate(names)])
