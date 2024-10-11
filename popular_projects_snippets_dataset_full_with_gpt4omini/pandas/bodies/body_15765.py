# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_nlargest.py
# helper function for 'test_boundary_{dtype}' tests
ser = Series(vals, dtype=dtype)
result = getattr(ser, method)(3)
expected_idxr = [0, 1, 2] if method == "nsmallest" else [3, 2, 1]
expected = ser.loc[expected_idxr]
tm.assert_series_equal(result, expected)
