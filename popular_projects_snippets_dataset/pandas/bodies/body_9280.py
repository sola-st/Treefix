# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
idx = period_range("2015-01-01", freq="D", periods=3)
result = Categorical(idx)
tm.assert_index_equal(result.categories, idx)

result = Categorical(Series(idx))
tm.assert_index_equal(result.categories, idx)
