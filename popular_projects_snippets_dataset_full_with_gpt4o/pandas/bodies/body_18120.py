# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_period.py
left = PeriodIndex([Period("2011-01-01"), pd.NaT, Period("2011-01-03")])
right = PeriodIndex([pd.NaT, pd.NaT, Period("2011-01-03")])

if dtype is not None:
    left = left.astype(dtype)
    right = right.astype(dtype)

result = left == right
expected = np.array([False, False, True])
tm.assert_numpy_array_equal(result, expected)

result = left != right
expected = np.array([True, True, False])
tm.assert_numpy_array_equal(result, expected)

expected = np.array([False, False, False])
tm.assert_numpy_array_equal(left == pd.NaT, expected)
tm.assert_numpy_array_equal(pd.NaT == right, expected)

expected = np.array([True, True, True])
tm.assert_numpy_array_equal(left != pd.NaT, expected)
tm.assert_numpy_array_equal(pd.NaT != left, expected)

expected = np.array([False, False, False])
tm.assert_numpy_array_equal(left < pd.NaT, expected)
tm.assert_numpy_array_equal(pd.NaT > left, expected)
