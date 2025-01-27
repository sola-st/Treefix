# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_period.py
arr = PeriodArray(np.arange(3), freq="D")
expected = PeriodArray(expected, freq="D")
arr[key] = value
tm.assert_period_array_equal(arr, expected)
