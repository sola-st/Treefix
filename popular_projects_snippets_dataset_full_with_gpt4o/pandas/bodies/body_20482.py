# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
# Compute a bool indexer to identify the positions to take.
# If we have an existing indexer, we only need to examine the
# subset of positions where the existing indexer is True.
if indexer is not None:
    # we only need to look at the subset of codes where the
    # existing indexer equals True
    codes = codes[indexer]

if step is None or step == 1:
    new_indexer = (codes >= start) & (codes < stop)
else:
    r = np.arange(start, stop, step, dtype=codes.dtype)
    new_indexer = algos.isin(codes, r)

if indexer is None:
    exit(new_indexer)

indexer = indexer.copy()
indexer[indexer] = new_indexer
exit(indexer)
