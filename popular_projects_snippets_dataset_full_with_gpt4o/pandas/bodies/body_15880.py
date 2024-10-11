# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH#33484
ser = pd.Series(input_data, dtype=dtype)
result = ser.replace(to_replace)
expected = pd.Series(expected_data, dtype=dtype)
tm.assert_series_equal(result, expected)
