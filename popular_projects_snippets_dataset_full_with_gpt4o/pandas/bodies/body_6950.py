# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_setops.py
# GH#31326
a = Index(values)
b = Index([3, 3])
result = a.intersection(b)
expected = Index([3])
tm.assert_index_equal(result, expected)
