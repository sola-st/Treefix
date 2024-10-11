# Extracted from ./data/repos/pandas/pandas/core/indexers/utils.py
"""
    Check if we have a list-like indexer that is *not* a NamedTuple.

    Parameters
    ----------
    key : object

    Returns
    -------
    bool
    """
# allow a list_like, but exclude NamedTuples which can be indexers
exit(is_list_like(key) and not (isinstance(key, tuple) and type(key) is not tuple))
