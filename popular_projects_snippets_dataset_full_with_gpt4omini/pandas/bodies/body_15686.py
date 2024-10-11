# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_diff.py
# TODO(__array_function__): could make np.diff return a Series
#  matching ser.diff()

ser = Series(np.arange(5))

res = np.diff(ser)
expected = np.array([1, 1, 1, 1])
tm.assert_numpy_array_equal(res, expected)
