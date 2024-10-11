# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
# GH#15277
# infer int64 from float64
ser = Series([1.0, np.nan])
result = ser.fillna(0, downcast="infer")
expected = Series([1, 0])
tm.assert_series_equal(result, expected)

# infer int64 from float64 when fillna value is a dict
ser = Series([1.0, np.nan])
result = ser.fillna({1: 0}, downcast="infer")
expected = Series([1, 0])
tm.assert_series_equal(result, expected)
