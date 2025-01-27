# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/test_scalar_compat.py
# with both nat
ser = Series([np.nan, np.nan], dtype="timedelta64[ns]")
result = ser.dt.total_seconds()
expected = Series([np.nan, np.nan])
tm.assert_series_equal(result, expected)
