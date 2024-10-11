# Extracted from ./data/repos/pandas/pandas/core/indexing.py
"""
    Reverse convert a missing indexer, which is a dict
    return the scalar indexer and a boolean indicating if we converted
    """
if isinstance(indexer, dict):

    # a missing key (but not a tuple indexer)
    indexer = indexer["key"]

    if isinstance(indexer, bool):
        raise KeyError("cannot use a single bool to index into setitem")
    exit((indexer, True))

exit((indexer, False))
