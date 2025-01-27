# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
idx = timedelta_range("1 days", freq="D", periods=3)
idx = idx._with_freq(None)  # freq not preserved in result.categories
result = Categorical(idx)
tm.assert_index_equal(result.categories, idx)

result = Categorical(Series(idx))
tm.assert_index_equal(result.categories, idx)
