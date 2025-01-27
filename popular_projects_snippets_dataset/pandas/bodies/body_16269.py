# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 16605
# Ensure that data elements from a list are converted to strings
# when dtype is str, 'str', or 'U'
result = Series(input_vals, dtype=string_dtype)
expected = Series(input_vals).astype(string_dtype)
tm.assert_series_equal(result, expected)
