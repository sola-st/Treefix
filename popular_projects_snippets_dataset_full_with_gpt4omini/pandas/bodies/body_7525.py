# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_duplicates.py
# GH 9125
n, k = 200, 5000
levels = [np.arange(n), tm.makeStringIndex(n), 1000 + np.arange(n)]
codes = [np.random.choice(n, k * n) for lev in levels]
mi = MultiIndex(levels=levels, codes=codes)

result = mi.duplicated(keep=keep)
expected = hashtable.duplicated(mi.values, keep=keep)
tm.assert_numpy_array_equal(result, expected)
