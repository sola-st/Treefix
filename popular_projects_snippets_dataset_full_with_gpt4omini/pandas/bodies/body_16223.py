# Extracted from ./data/repos/pandas/pandas/tests/series/test_missing.py
ts = datetime_series.copy()
ts.index = ts.index._with_freq(None)
ts[::2] = np.NaN

result = ts.dropna()
assert len(result) == ts.count()
tm.assert_series_equal(result, ts[1::2])
tm.assert_series_equal(result, ts[pd.notna(ts)])
