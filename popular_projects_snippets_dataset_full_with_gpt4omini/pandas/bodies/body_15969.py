# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_value_counts.py
# GH 17927
result = Series(input_array).value_counts()
tm.assert_series_equal(result, expected)
