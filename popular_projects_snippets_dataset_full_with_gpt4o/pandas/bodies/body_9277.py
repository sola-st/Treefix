# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
idx = date_range("2015-01-01 10:00", freq="D", periods=3, tz="US/Eastern")
idx = idx._with_freq(None)  # freq not preserved in result.categories
result = Categorical(idx)
tm.assert_index_equal(result.categories, idx)

result = Categorical(Series(idx))
tm.assert_index_equal(result.categories, idx)
