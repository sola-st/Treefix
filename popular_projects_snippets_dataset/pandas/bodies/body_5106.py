# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#21980
now = Timestamp("2021-11-09 09:54:00")
arr = np.array([now, Timedelta("1D"), np.timedelta64(2, "h")])
exp = np.array(
    [
        now - Timedelta("1D"),
        Timedelta("0D"),
        np.timedelta64(2, "h") - Timedelta("1D"),
    ]
)
res = arr - Timedelta("1D")
tm.assert_numpy_array_equal(res, exp)
