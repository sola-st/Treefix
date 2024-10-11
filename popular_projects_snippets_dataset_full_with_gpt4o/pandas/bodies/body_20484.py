# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
if isinstance(indexer, slice):
    new_indexer = np.zeros(n, dtype=np.bool_)
    new_indexer[indexer] = True
    exit(new_indexer)
exit(indexer)
