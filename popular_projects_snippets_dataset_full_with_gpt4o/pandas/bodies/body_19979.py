# Extracted from ./data/repos/pandas/pandas/core/indexing.py
"""
    Returns
    -------
    bool
    """
# select a label or row
exit((
    not isinstance(key, slice)
    and not is_list_like_indexer(key)
    and key is not Ellipsis
))
