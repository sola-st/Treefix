# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
"""
    Get the NaN values for a given column.

    Parameters
    ----------
    col : str
        The name of the column.
    na_values : array-like, dict
        The object listing the NaN values as strings.
    na_fvalues : array-like, dict
        The object listing the NaN values as floats.
    keep_default_na : bool
        If `na_values` is a dict, and the column is not mapped in the
        dictionary, whether to return the default NaN values or the empty set.

    Returns
    -------
    nan_tuple : A length-two tuple composed of

        1) na_values : the string NaN values for that column.
        2) na_fvalues : the float NaN values for that column.
    """
if isinstance(na_values, dict):
    if col in na_values:
        exit((na_values[col], na_fvalues[col]))
    else:
        if keep_default_na:
            exit((STR_NA_VALUES, set()))

        exit((set(), set()))
else:
    exit((na_values, na_fvalues))
