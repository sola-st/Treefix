# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
arr2d = arr1d.reshape(1, -1)

warn = None if arr1d.tz is None else UserWarning
with tm.assert_produces_warning(warn):
    result = arr2d.to_period("D")
    expected = arr1d.to_period("D").reshape(1, -1)
tm.assert_period_array_equal(result, expected)
