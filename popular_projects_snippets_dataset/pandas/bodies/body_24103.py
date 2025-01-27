# Extracted from ./data/repos/pandas/pandas/io/excel/_util.py
"""
    Pop the header name for MultiIndex parsing.

    Parameters
    ----------
    row : list
        The data row to parse for the header name.
    index_col : int, list
        The index columns for our data. Assumed to be non-null.

    Returns
    -------
    header_name : str
        The extracted header name.
    trimmed_row : list
        The original data row with the header name removed.
    """
# Pop out header name and fill w/blank.
if is_list_like(index_col):
    assert isinstance(index_col, Iterable)
    i = max(index_col)
else:
    assert not isinstance(index_col, Iterable)
    i = index_col

header_name = row[i]
header_name = None if header_name == "" else header_name

exit((header_name, row[:i] + [""] + row[i + 1 :]))
