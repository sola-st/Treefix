# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# Case where we having a NaT in the result inseat of timedelta64("NaT")
#  is misleading
orig = timedelta_range("1 Day", periods=3).insert(1, NaT)
tdi = tm.box_expected(orig, box_with_array, transpose=False)

other = np.array([orig[0], 1.5, 2.0, orig[2]], dtype=object)
other = tm.box_expected(other, box_with_array, transpose=False)

res = tdi / other

expected = pd.Index(
    [1.0, np.timedelta64("NaT", "ns"), orig[0], 1.5], dtype=object
)
expected = tm.box_expected(expected, box_with_array, transpose=False)
if isinstance(expected, PandasArray):
    expected = expected.to_numpy()
tm.assert_equal(res, expected)
if box_with_array is DataFrame:
    # We have a np.timedelta64(NaT), not pd.NaT
    assert isinstance(res.iloc[1, 0], np.timedelta64)

res = tdi // other

expected = pd.Index([1, np.timedelta64("NaT", "ns"), orig[0], 1], dtype=object)
expected = tm.box_expected(expected, box_with_array, transpose=False)
if isinstance(expected, PandasArray):
    expected = expected.to_numpy()
tm.assert_equal(res, expected)
if box_with_array is DataFrame:
    # We have a np.timedelta64(NaT), not pd.NaT
    assert isinstance(res.iloc[1, 0], np.timedelta64)
