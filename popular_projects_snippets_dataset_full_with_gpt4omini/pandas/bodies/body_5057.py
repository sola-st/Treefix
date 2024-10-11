# Extracted from ./data/repos/pandas/pandas/tests/scalar/interval/test_interval.py
# https://github.com/pandas-dev/pandas/issues/35931
interval = Interval(0, 1)
arr = np.array([interval, interval])
result = interval == arr
expected = np.array([True, True])
tm.assert_numpy_array_equal(result, expected)
