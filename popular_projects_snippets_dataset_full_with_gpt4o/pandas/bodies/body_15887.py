# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH#48231
ser = pd.Series([1, val])
result = ser.replace(val, None)
expected = pd.Series([1, None], dtype=object)
tm.assert_series_equal(result, expected)
