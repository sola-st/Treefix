# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
# GH#36289
a = Index([0, 0, 1])
b = Index([0, 0, 1, 2])
result = a.union(b)
expected = Index([0, 0, 1, 2])
tm.assert_index_equal(result, expected)
