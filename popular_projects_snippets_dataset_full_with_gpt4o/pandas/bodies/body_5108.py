# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#21980
arr = np.array([Timestamp("20130101 9:01"), Timestamp("20121230 9:02")])
exp = np.array([Timestamp("20130102 9:01"), Timestamp("20121231 9:02")])
res = op(arr, Timedelta("1D"))
tm.assert_numpy_array_equal(res, exp)
