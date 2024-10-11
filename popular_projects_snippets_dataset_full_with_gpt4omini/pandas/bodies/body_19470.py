# Extracted from ./data/repos/pandas/pandas/core/internals/construction.py
"""
    If columns is None, make numbers as column names; Otherwise, validate that
    columns have valid length.

    Parameters
    ----------
    content : list of np.ndarrays
    columns : Index or None

    Returns
    -------
    Index
        If columns is None, assign positional column index value as columns.

    Raises
    ------
    1. AssertionError when content is not composed of list of lists, and if
        length of columns is not equal to length of content.
    2. ValueError when content is list of lists, but length of each sub-list
        is not equal
    3. ValueError when content is list of lists, but length of sub-list is
        not equal to length of content
    """
if columns is None:
    columns = default_index(len(content))
else:

    # Add mask for data which is composed of list of lists
    is_mi_list = isinstance(columns, list) and all(
        isinstance(col, list) for col in columns
    )

    if not is_mi_list and len(columns) != len(content):  # pragma: no cover
        # caller's responsibility to check for this...
        raise AssertionError(
            f"{len(columns)} columns passed, passed data had "
            f"{len(content)} columns"
        )
    if is_mi_list:

        # check if nested list column, length of each sub-list should be equal
        if len({len(col) for col in columns}) > 1:
            raise ValueError(
                "Length of columns passed for MultiIndex columns is different"
            )

        # if columns is not empty and length of sublist is not equal to content
        if columns and len(columns[0]) != len(content):
            raise ValueError(
                f"{len(columns[0])} columns passed, passed data had "
                f"{len(content)} columns"
            )
exit(columns)
