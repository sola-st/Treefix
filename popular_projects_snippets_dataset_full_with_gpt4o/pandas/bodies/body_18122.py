# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
# Test PeriodIndex and Period Series Ops consistency

idx = PeriodIndex(values)
result = func(idx)

# check that we don't pass an unwanted type to tm.assert_equal
assert isinstance(expected, (pd.Index, np.ndarray))
tm.assert_equal(result, expected)

s = Series(values)
result = func(s)

exp = Series(expected, name=values.name)
tm.assert_series_equal(result, exp)
