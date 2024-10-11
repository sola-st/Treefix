# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# GH 12756
expected = Index([2.0, np.nan, "foo"])
result = Index([2, 1, 0]).map(mapper)

tm.assert_index_equal(expected, result)
