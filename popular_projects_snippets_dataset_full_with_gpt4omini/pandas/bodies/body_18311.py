# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
left = TimedeltaIndex([Timedelta("1 days"), NaT, Timedelta("3 days")])
right = TimedeltaIndex([NaT, NaT, Timedelta("3 days")])

lhs, rhs = left, right
if dtype is object:
    lhs, rhs = left.astype(object), right.astype(object)

result = rhs == lhs
expected = np.array([False, False, True])
tm.assert_numpy_array_equal(result, expected)

result = rhs != lhs
expected = np.array([True, True, False])
tm.assert_numpy_array_equal(result, expected)

expected = np.array([False, False, False])
tm.assert_numpy_array_equal(lhs == NaT, expected)
tm.assert_numpy_array_equal(NaT == rhs, expected)

expected = np.array([True, True, True])
tm.assert_numpy_array_equal(lhs != NaT, expected)
tm.assert_numpy_array_equal(NaT != lhs, expected)

expected = np.array([False, False, False])
tm.assert_numpy_array_equal(lhs < NaT, expected)
tm.assert_numpy_array_equal(NaT > lhs, expected)
