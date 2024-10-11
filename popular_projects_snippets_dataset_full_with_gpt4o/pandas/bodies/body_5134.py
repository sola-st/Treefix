# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#18846
td = Timedelta(hours=3, minutes=4)
scalar = Timedelta(hours=3, minutes=3)

# Array-like others
assert td // np.array(scalar.to_timedelta64()) == 1

res = (3 * td) // np.array([scalar.to_timedelta64()])
expected = np.array([3], dtype=np.int64)
tm.assert_numpy_array_equal(res, expected)

res = (10 * td) // np.array([scalar.to_timedelta64(), np.timedelta64("NaT")])
expected = np.array([10, np.nan])
tm.assert_numpy_array_equal(res, expected)
