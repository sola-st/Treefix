# Extracted from ./data/repos/pandas/pandas/tests/arithmetic/test_timedelta64.py
# GH#26689 should unbox when comparing with zerodim array
box = box_with_array
xbox = (
    box_with_array if box_with_array not in [pd.Index, pd.array] else np.ndarray
)

tdi = timedelta_range("2H", periods=4)
other = np.array(tdi.to_numpy()[0])

tdi = tm.box_expected(tdi, box)
res = tdi <= other
expected = np.array([True, False, False, False])
expected = tm.box_expected(expected, xbox)
tm.assert_equal(res, expected)
