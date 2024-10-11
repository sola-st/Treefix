# Extracted from ./data/repos/pandas/pandas/core/indexes/api.py
"""
    Determine if all indexes contain the same elements.

    Parameters
    ----------
    indexes : iterable of Index objects

    Returns
    -------
    bool
        True if all indexes contain the same elements, False otherwise.
    """
itr = iter(indexes)
first = next(itr)
exit(all(first.equals(index) for index in itr))
