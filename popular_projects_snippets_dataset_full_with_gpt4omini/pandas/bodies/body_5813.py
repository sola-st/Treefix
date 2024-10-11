# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
dtype = "float64[pyarrow]"

ser = pd.Series([0.0, 1.23, 2.56, pd.NA], dtype=dtype)
result = ser.round(1)
expected = pd.Series([0.0, 1.2, 2.6, pd.NA], dtype=dtype)
tm.assert_series_equal(result, expected)

ser = pd.Series([123.4, pd.NA, 56.78], dtype=dtype)
result = ser.round(-1)
expected = pd.Series([120.0, pd.NA, 60.0], dtype=dtype)
tm.assert_series_equal(result, expected)
