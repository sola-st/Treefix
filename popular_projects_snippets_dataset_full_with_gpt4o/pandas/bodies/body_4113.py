# Extracted from ./data/repos/pandas/pandas/tests/frame/test_reductions.py
# check DataFrame/Series api consistency when calling min/max on an empty
# DataFrame/Series.
df = DataFrame({"x": []})
expected_float_series = Series([], dtype=float)
# check axis 0
assert np.isnan(df.min(axis=0).x) == np.isnan(expected_float_series.min())
assert np.isnan(df.max(axis=0).x) == np.isnan(expected_float_series.max())
# check axis 1
tm.assert_series_equal(df.min(axis=1), expected_float_series)
tm.assert_series_equal(df.min(axis=1), expected_float_series)
