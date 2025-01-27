# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
# GH 19729
expected = Series([val])
result = to_numeric(expected, downcast="float")
tm.assert_series_equal(result, expected)
