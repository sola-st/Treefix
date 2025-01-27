# Extracted from ./data/repos/pandas/pandas/tests/series/test_cumulative.py
ufunc = methods[method]

result = getattr(datetime_series, method)().values
expected = ufunc(np.array(datetime_series))

tm.assert_numpy_array_equal(result, expected)
ts = datetime_series.copy()
ts[::2] = np.NaN
result = getattr(ts, method)()[1::2]
expected = ufunc(ts.dropna())

result.index = result.index._with_freq(None)
tm.assert_series_equal(result, expected)
