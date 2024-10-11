# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# https://github.com/pandas-dev/pandas/issues/45858
ser = Series(data)
with tm.assert_produces_warning(None):
    result = ser.dt.strftime("%Y-%m-%d")
expected = Series([np.nan], dtype=object)
tm.assert_series_equal(result, expected)
