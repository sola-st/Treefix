# Extracted from ./data/repos/pandas/pandas/tests/series/test_cumulative.py
# GH#6270
# checking Series method vs the ufunc applied to the values

ser = func(pd.Series(arg))
ufunc = methods[method]

exp_vals = ufunc(ser.values)
expected = pd.Series(exp_vals)

result = getattr(ser, method)()

tm.assert_series_equal(result, expected)
