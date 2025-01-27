# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
# GH#36289
a = Index([np.nan, 1, 2, 2])
b = Index([np.nan, dup, 1, 2])
result = a.union(b, sort=False)
expected = Index([np.nan, dup, 1.0, 2.0, 2.0])
tm.assert_index_equal(result, expected)
