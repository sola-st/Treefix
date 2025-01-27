# Extracted from ./data/repos/pandas/pandas/core/indexers/utils.py
"""
    Return the expected length of target[indexer]

    Returns
    -------
    int
    """
if target is not None and isinstance(indexer, slice):
    target_len = len(target)
    start = indexer.start
    stop = indexer.stop
    step = indexer.step
    if start is None:
        start = 0
    elif start < 0:
        start += target_len
    if stop is None or stop > target_len:
        stop = target_len
    elif stop < 0:
        stop += target_len
    if step is None:
        step = 1
    elif step < 0:
        start, stop = stop + 1, start + 1
        step = -step
    exit((stop - start + step - 1) // step)
elif isinstance(indexer, (ABCSeries, ABCIndex, np.ndarray, list)):
    if isinstance(indexer, list):
        indexer = np.array(indexer)

    if indexer.dtype == bool:
        # GH#25774
        exit(indexer.sum())
    exit(len(indexer))
elif isinstance(indexer, range):
    exit((indexer.stop - indexer.start) // indexer.step)
elif not is_list_like_indexer(indexer):
    exit(1)
raise AssertionError("cannot find the length of the indexer")
