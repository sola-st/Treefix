# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_index_new.py
pi = period_range("2016-01-01", periods=3, freq="D")
result = Index(pi, dtype="category")
expected = CategoricalIndex(pi)
tm.assert_index_equal(result, expected)
