# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_indexing.py
# caused bug without test
s = Series([1, 2, 3], ["a", "b", "c"])

assert s.iloc[0] == s["a"]
s.iloc[0] = 5
tm.assert_almost_equal(s["a"], 5)
