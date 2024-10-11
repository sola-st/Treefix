# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#23215
other = np.datetime64("NaT")

tdi = timedelta_range("1 day", periods=3)
expected = DatetimeIndex(["NaT", "NaT", "NaT"])

tdser = tm.box_expected(tdi, box_with_array)
expected = tm.box_expected(expected, box_with_array)

tm.assert_equal(tdser + other, expected)
tm.assert_equal(other + tdser, expected)
