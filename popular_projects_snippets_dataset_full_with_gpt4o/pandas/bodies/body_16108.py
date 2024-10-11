# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH 29578
ser = Series(data)
result = ser.dt.strftime("%Y-%m-%d")
expected = Series(["2019-01-01", np.nan])
tm.assert_series_equal(result, expected)
