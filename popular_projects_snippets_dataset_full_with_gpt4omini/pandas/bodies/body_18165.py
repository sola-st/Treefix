# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
idx = PeriodIndex(values)
result = func(idx)
tm.assert_equal(result, expected)

ser = Series(values)
result = func(ser)

exp = Series(expected, name=values.name)
tm.assert_series_equal(result, exp)
