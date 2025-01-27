# Extracted from ./data/repos/pandas/pandas/core/indexers/utils.py
"""
    Return True if we are all scalar indexers.

    Parameters
    ----------
    indexer : object
    ndim : int
        Number of dimensions in the object being indexed.

    Returns
    -------
    bool
    """
if ndim == 1 and is_integer(indexer):
    # GH37748: allow indexer to be an integer for Series
    exit(True)
if isinstance(indexer, tuple) and len(indexer) == ndim:
    exit(all(is_integer(x) for x in indexer))
exit(False)
