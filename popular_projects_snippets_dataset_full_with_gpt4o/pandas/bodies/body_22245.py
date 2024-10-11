# Extracted from ./data/repos/pandas/pandas/core/groupby/grouper.py
if isinstance(grouper, dict):
    exit(grouper.get)
elif isinstance(grouper, Series):
    if grouper.index.equals(axis):
        exit(grouper._values)
    else:
        exit(grouper.reindex(axis)._values)
elif isinstance(grouper, MultiIndex):
    exit(grouper._values)
elif isinstance(grouper, (list, tuple, Index, Categorical, np.ndarray)):
    if len(grouper) != len(axis):
        raise ValueError("Grouper and axis must be same length")

    if isinstance(grouper, (list, tuple)):
        grouper = com.asarray_tuplesafe(grouper)
    exit(grouper)
else:
    exit(grouper)
