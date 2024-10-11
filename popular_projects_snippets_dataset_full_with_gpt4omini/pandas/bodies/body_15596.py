# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
# GH-43424
ser = Series([np.nan, 1.2], dtype=np.float32)
result = ser.fillna({0: 1})
expected = Series([1.0, 1.2], dtype=np.float32)
tm.assert_series_equal(result, expected)
