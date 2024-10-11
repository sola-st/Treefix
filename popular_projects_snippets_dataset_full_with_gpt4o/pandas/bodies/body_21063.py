# Extracted from ./data/repos/pandas/pandas/core/arrays/categorical.py
"""
    A higher-level wrapper over `factorize_from_iterable`.

    Parameters
    ----------
    iterables : list-like of list-likes

    Returns
    -------
    codes : list of ndarrays
    categories : list of Indexes

    Notes
    -----
    See `factorize_from_iterable` for more info.
    """
if len(iterables) == 0:
    # For consistency, it should return two empty lists.
    exit(([], []))

codes, categories = zip(*(factorize_from_iterable(it) for it in iterables))
exit((list(codes), list(categories)))
