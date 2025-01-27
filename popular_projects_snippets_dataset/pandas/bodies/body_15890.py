# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH#50758
ser = pd.Series([val, 1])
expected = pd.Series([val, pd.NA])
result = ser.replace(to_replace=1, value=pd.NA)
tm.assert_series_equal(result, expected)

ser.replace(to_replace=1, value=pd.NA, inplace=True)
tm.assert_series_equal(ser, expected)
