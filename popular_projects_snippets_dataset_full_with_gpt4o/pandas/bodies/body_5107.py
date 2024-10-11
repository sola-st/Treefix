# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_arithmetic.py
# GH#21980
now = Timestamp("2021-11-09 09:54:00")
arr = np.array([now, Timedelta("1D"), np.timedelta64(2, "h")])
msg = r"unsupported operand type\(s\) for \-: 'Timedelta' and 'Timestamp'"
with pytest.raises(TypeError, match=msg):
    Timedelta("1D") - arr
