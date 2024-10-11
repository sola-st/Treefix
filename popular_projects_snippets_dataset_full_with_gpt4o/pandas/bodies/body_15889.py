# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH#47480
ser = pd.Series([0, 1, pd.NA], dtype=dtype)
expected = pd.Series([0, 2, pd.NA], dtype=dtype)
result = ser.replace(to_replace=1, value=2)
tm.assert_series_equal(result, expected)

ser.replace(to_replace=1, value=2, inplace=True)
tm.assert_series_equal(ser, expected)
