# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#18846
td = Timedelta(hours=3, minutes=3)
scalar = Timedelta(hours=3, minutes=4)

# Array-like others
assert td.__rfloordiv__(np.array(scalar.to_timedelta64())) == 1

res = td.__rfloordiv__(np.array([(3 * scalar).to_timedelta64()]))
expected = np.array([3], dtype=np.int64)
tm.assert_numpy_array_equal(res, expected)

arr = np.array([(10 * scalar).to_timedelta64(), np.timedelta64("NaT")])
res = td.__rfloordiv__(arr)
expected = np.array([10, np.nan])
tm.assert_numpy_array_equal(res, expected)
