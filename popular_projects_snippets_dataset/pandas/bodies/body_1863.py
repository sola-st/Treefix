# Extracted from ./data/repos/pandas/pandas/tests/resample/test_resample_api.py
# GH#31710 cython needs to allow readonly data
index = date_range("2020-01-01", "2020-01-02", freq="1h")
arr = np.zeros_like(index)
arr.setflags(write=False)

ser = Series(arr, index=index)
rs = ser.resample("1D")

expected = Series([pd.Timestamp(0), pd.Timestamp(0)], index=index[::24])

result = rs.agg("last")
tm.assert_series_equal(result, expected)

result = rs.agg("first")
tm.assert_series_equal(result, expected)

result = rs.agg("max")
tm.assert_series_equal(result, expected)

result = rs.agg("min")
tm.assert_series_equal(result, expected)
