# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH#43018
result = Series(index=[0], dtype="bool")
expected = Series(True, index=[0], dtype="bool")
tm.assert_series_equal(result, expected)
