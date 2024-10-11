# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#14155
ser = Series(10 * [np.timedelta64(10, "m")])
ser.loc[[1, 2, 3]] = np.timedelta64(20, "m")
expected = Series(10 * [np.timedelta64(10, "m")])
expected.loc[[1, 2, 3]] = Timedelta(np.timedelta64(20, "m"))
tm.assert_series_equal(ser, expected)
