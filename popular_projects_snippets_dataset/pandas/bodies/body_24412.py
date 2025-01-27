# Extracted from ./data/repos/pandas/pandas/io/parsers/readers.py
"""
    Raise ValueError if the `names` parameter contains duplicates or has an
    invalid data type.

    Parameters
    ----------
    names : array-like or None
        An array containing a list of the names used for the output DataFrame.

    Raises
    ------
    ValueError
        If names are not unique or are not ordered (e.g. set).
    """
if names is not None:
    if len(names) != len(set(names)):
        raise ValueError("Duplicate names are not allowed.")
    if not (
        is_list_like(names, allow_sets=False) or isinstance(names, abc.KeysView)
    ):
        raise ValueError("Names should be an ordered collection.")
