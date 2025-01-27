# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py

# M8
v1 = Timestamp("20130101 09:00:00.00004")
v2 = Timestamp("20130101")
x = Series([v1, v1, v1, v2, v2, v1])
codes, uniques = algos.factorize(x)

exp = np.array([0, 0, 0, 1, 1, 0], dtype=np.intp)
tm.assert_numpy_array_equal(codes, exp)
exp = DatetimeIndex([v1, v2])
tm.assert_index_equal(uniques, exp)

codes, uniques = algos.factorize(x, sort=True)
exp = np.array([1, 1, 1, 0, 0, 1], dtype=np.intp)
tm.assert_numpy_array_equal(codes, exp)
exp = DatetimeIndex([v2, v1])
tm.assert_index_equal(uniques, exp)

# period
v1 = Period("201302", freq="M")
v2 = Period("201303", freq="M")
x = Series([v1, v1, v1, v2, v2, v1])

# periods are not 'sorted' as they are converted back into an index
codes, uniques = algos.factorize(x)
exp = np.array([0, 0, 0, 1, 1, 0], dtype=np.intp)
tm.assert_numpy_array_equal(codes, exp)
tm.assert_index_equal(uniques, PeriodIndex([v1, v2]))

codes, uniques = algos.factorize(x, sort=True)
exp = np.array([0, 0, 0, 1, 1, 0], dtype=np.intp)
tm.assert_numpy_array_equal(codes, exp)
tm.assert_index_equal(uniques, PeriodIndex([v1, v2]))

# GH 5986
v1 = to_timedelta("1 day 1 min")
v2 = to_timedelta("1 day")
x = Series([v1, v2, v1, v1, v2, v2, v1])
codes, uniques = algos.factorize(x)
exp = np.array([0, 1, 0, 0, 1, 1, 0], dtype=np.intp)
tm.assert_numpy_array_equal(codes, exp)
tm.assert_index_equal(uniques, to_timedelta([v1, v2]))

codes, uniques = algos.factorize(x, sort=True)
exp = np.array([1, 0, 1, 1, 0, 0, 1], dtype=np.intp)
tm.assert_numpy_array_equal(codes, exp)
tm.assert_index_equal(uniques, to_timedelta([v2, v1]))
