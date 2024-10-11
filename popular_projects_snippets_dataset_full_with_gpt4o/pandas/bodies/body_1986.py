# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
ser = Series(["a", "b", "c"])
result = to_numeric(ser, errors="coerce")

expected = Series([np.nan, np.nan, np.nan])
tm.assert_series_equal(result, expected)
