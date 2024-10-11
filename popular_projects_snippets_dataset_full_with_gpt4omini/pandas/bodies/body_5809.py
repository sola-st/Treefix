# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
# GH50430
ser = pd.Series(["1.0"])
result = ser.astype("float64[pyarrow]")
expected = pd.Series([1.0], dtype="float64[pyarrow]")
tm.assert_series_equal(result, expected)
