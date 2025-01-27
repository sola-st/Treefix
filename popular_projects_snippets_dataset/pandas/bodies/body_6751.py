# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval.py
mask = [True, False] + [True] * 8
exit(IntervalIndex.from_arrays(
    np.where(mask, np.arange(10), np.nan),
    np.where(mask, np.arange(1, 11), np.nan),
    closed=closed,
))
