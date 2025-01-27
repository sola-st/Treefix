# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_astype.py
# GH#43018
ser = Series(np.nan, dtype="object")
result = ser.astype("bool")
expected = Series(True, dtype="bool")
tm.assert_series_equal(result, expected)
