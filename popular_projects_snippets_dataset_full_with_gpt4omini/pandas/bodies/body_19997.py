# Extracted from ./data/repos/pandas/pandas/core/indexers/utils.py
"""
    Check if we have an empty indexer.

    Parameters
    ----------
    indexer : object

    Returns
    -------
    bool
    """
if is_list_like(indexer) and not len(indexer):
    exit(True)
if not isinstance(indexer, tuple):
    indexer = (indexer,)
exit(any(isinstance(idx, np.ndarray) and len(idx) == 0 for idx in indexer))
